import requests, json
import argparse
def view_all(_num):
    url = 'http://localhost:2015/posts/all/recent/{num}'
    url = url.format(num = _num)
    r = requests.get(url)
    return r

def view_post(_community, _id):
    url = 'http://localhost:2015/posts/{community}/post/{id}'
    url = url.format(community = _community, id = _id)
    print(url)
    headers = {'content-type': 'application/json'}
    r = requests.get(url, headers=headers)
    return r

def view_post_url (url):
    print("http://localhost:2015"+ url)
    headers = {'content-type': 'application/json'}
    r = requests.get("http://localhost:2015"+url, headers=headers)
    return r

def view_by_community(_community, _num):
    url = 'http://localhost:2015/posts/{community}/recent/{num}'
    url = url.format(community = _community, num = _num)
    headers = {'content-type': 'application/json'}
    r = requests.get(url, headers=headers)
    return r

def new_post(_community, post):
    url = 'http://localhost:2015/posts/{community}/new'
    url = url.format(community = _community)
    with open(post, "r") as f:
        data = json.load(f)
    headers = {'content-type': 'application/json'}
    r = requests.post(url, json=data, headers=headers)
    return r

def delete_post(_community, _id):
    url = 'http://localhost:2015/posts/{community}/post/{id}'
    url = url.format(community = _community, id = _id)
    headers = {'content-type': 'application/json'}
    r = requests.delete(url, headers=headers)
    return r

def delete_post_url(url):
    headers = {'content-type': 'application/json'}
    r = requests.delete("http://localhost:2015"+url, headers=headers)
    return r

def upvote_post(_community, _id):
    url = 'http://localhost:2015/votes/{community}/post/{id}/upvote'
    url = url.format(community = _community, id = _id)
    headers = {'content-type': 'application/json'}
    r = requests.patch(url, headers=headers)
    return r
def upvote_post_url (url):
    print ("http://localhost:2015"+ url +"/upvote")
    headers = {'content-type': 'application/json'}
    r = requests.patch("http://localhost:2015"+ url+"/upvote", headers=headers)
    return r

def downvote_post(_community, _id):
    url = 'http://localhost:2015/votes/{community}/post/{id}/downvote'
    url = url.format(community = _community, id = _id)
    headers = {'content-type': 'application/json'}
    r = requests.patch(url, headers=headers)
    return r
def downvote_post_url (url):
    print ("http://localhost:2015"+ url +"/downvote")
    headers = {'content-type': 'application/json'}
    r = requests.patch("http://localhost:2015"+ url +"/downvote", headers=headers)
    return r

def get_score(_community, _id):
    url = 'http://localhost:2015/votes/{community}/post/{id}/score'
    url = url.format(community = _community, id = _id)
    headers = {'content-type': 'application/json'}
    r = requests.get(url, headers=headers)
    return r

def get_score_url(url):
    headers = {'content-type': 'application/json'}
    r = requests.get("http://localhost:2015"+ url +"/score", headers=headers)
    return r

def top_posts(_num):
    url = 'http://localhost:2015/votes/all/top/{num}'
    url = url.format(num = _num)
    headers = {'content-type': 'application/json'}
    r = requests.get(url, headers=headers)
    return r

def order_posts(json_obj):
    url = 'http://localhost:2015/votes/list/top'
    headers = {'content-type': 'application/json'}
    r = requests.get(url, json = json_obj, headers=headers)
    return r



def main():
    list_of_urls = []
    hostname = "http://localhost:2015"
    parser = argparse.ArgumentParser(description='CPSC 121 Lab exercise grader')
    parser.add_argument('-v', '--verbose', action = 'store_true', default = False, help = "Only turn this on if you want to see a lot of json")
    args = parser.parse_args()
    print("---------------------------------------------------------\n")
    print("POSTS\n")
    print("---------------------------------------------------------\n")
    """
        Trying to view a post before it exists will correctly return a error 400
    """
    print("1. Attempt to view a post before any posts are made")
    resp = view_post("DoesNotExist", "1")
    assert resp.status_code == 400, 'FAIL - Expected status code 400. Got status code' + str(resp.status_code)
    print("PASS - status code returns 400 because there is no posts to view in the DoesNotExist Community")

    """
        Create and view posts
    """
    print("\n2. Create a new post with no link\n")
    print("a. Create the post")
    resp = new_post("CSUF-CPSC449", "json/new_post1.json")
    print(resp.json())
    assert resp.status_code == 201, 'FAIL - Expected status code 201. Got status code' + str(resp.status_code)
    print(resp.json())
    list_of_urls.append(resp.json()['url'])
    print("PASS - post created")
    print("b. view the post")
    resp = view_post_url(resp.json()['url'])
    assert resp.status_code == 200, 'FAIL - Expected status code 200. Got status code' + str(resp.status_code)+ " And got " + str(resp.json())
    print(resp.json())

    print("\n3. Create a new post with a link\n")
    print("a. Create the post")
    resp = new_post("Mechanical_Keyboards", "json/new_post_w_url2.json")
    assert resp.status_code == 201, 'FAIL - Expected status code 201. Got status code' + str(resp.status_code)
    print(resp.json())
    print("PASS - post created")
    print("b. view the post")
    delete_post_ex = resp.json()['url']
    resp = view_post_url(resp.json()['url'])
    assert resp.status_code == 200, 'FAIL - Expected status code 200. Got status code' + str(resp.status_code)
    print(resp.json())


    """
        INSERT MANY MORE POSTS FOR THE OTHER ENDPOINT TESTING
    """
    print("\nInsert Many posts for testing of the rest of the posting endpoints \n")

    resp = new_post("CSUF-CPSC449", "json/new_post2.json")
    assert resp.status_code == 201, 'FAIL - Expected status code 201. Got status code' + str(resp.status_code)
    print("PASS - post created")
    list_of_urls.append(resp.json()['url'])

    resp = new_post("CSUF-CPSC449", "json/new_post3.json")
    assert resp.status_code == 201, 'FAIL - Expected status code 201. Got status code' + str(resp.status_code)
    print("PASS - post created")
    list_of_urls.append(resp.json()['url'])

    resp = new_post("CSUF-CPSC449", "json/new_post4.json")
    assert resp.status_code == 201, 'FAIL - Expected status code 201. Got status code' + str(resp.status_code)
    print("PASS - post created")
    list_of_urls.append(resp.json()['url'])

    resp = new_post("CSUF-CPSC449", "json/new_post5.json")
    assert resp.status_code == 201, 'FAIL - Expected status code 201. Got status code' + str(resp.status_code)
    print("PASS - post created")
    list_of_urls.append(resp.json()['url'])

    resp = new_post("CSUF-CPSC449", "json/new_post6.json")
    assert resp.status_code == 201, 'FAIL - Expected status code 201. Got status code' + str(resp.status_code)
    print("PASS - post created")
    list_of_urls.append(resp.json()['url'])

    resp = new_post("CSUF-CPSC449", "json/new_post7.json")
    assert resp.status_code == 201, 'FAIL - Expected status code 201. Got status code' + str(resp.status_code)
    print("PASS - post created")
    list_of_urls.append(resp.json()['url'])

    """
        LIST N MOST RECENT POST FOR ALL COMMUNITIES
    """
    print( "\n4 - List the n most recent posts to any community\n")
    print( " n = 3 ")
    resp = view_all(3)
    assert resp.status_code == 200, 'FAIL - Expected status code 200. Got status code' + str(resp.status_code)
    assert len(resp.json()['data']) == 3 , "FAIL - Expected the length of the json to be 3. Instead received" + str(len(resp.json()["data"]))
    print("PASS - view all last 3 posts returned 3 posts")
    if(args.verbose):
        print(resp.json()['data'])

    print( " n = 5 ")
    resp = view_all(5)
    assert resp.status_code == 200, 'FAIL - Expected status code 200. Got status code' + str(resp.status_code)
    assert len(resp.json()['data']) == 5 , "FAIL - Expected the length of the json to be 5. Instead received" + str(len(resp.json()["data"]))
    print("PASS - view all last 5 posts returned 5 posts")
    if(args.verbose):
        print(resp.json()['data'])

    """
        LIST N MOST RECENT POST FOR A PARTICULAR COMMUNITY
    """
    print( "\n5 - List the n most recent posts to a particular community\n")
    print( " In this case the particular community is CSUF-CPSC449")
    print( " n = 3 ")
    resp = view_by_community("CSUF-CPSC449","3")
    assert resp.status_code == 200, 'FAIL - Expected status code 200. Got status code' + str(resp.status_code)
    assert len(resp.json()['data']) == 3 , "FAIL - Expected the length of the json to be 3. Instead received" + str(len(resp.json()["data"]))
    print("PASS - view all last 3 posts returned 3 posts")
    if(args.verbose):
        print(resp.json()['data'])

    print( " n = 5 ")
    resp = view_by_community("CSUF-CPSC449","5")
    assert resp.status_code == 200, 'FAIL - Expected status code 200. Got status code' + str(resp.status_code)
    assert len(resp.json()['data']) == 5 , "FAIL - Expected the length of the json to be 5. Instead received" + str(len(resp.json()["data"]))
    print("PASS - view all last 5 posts returned 5 posts")
    if(args.verbose):
        print(resp.json()['data'])

    """
        DELETE POST
    """
    print("\n6 - Delete a post\n")
    print(" If this post is ran on a blank posts.db then there should only be one post in the\nMechanical Keyboards Community")
    resp = view_by_community("Mechanical_Keyboards","1")
    print(resp.json())
    print(" We will now delete it")
    resp = delete_post_url(delete_post_ex)
    assert resp.status_code == 200, 'FAIL - Expected status code 200. Got status code' + str(resp.status_code)
    print("PASS -  Delete returned 200")
    print("now there are no more posts in Mechanical_Keyboards :(")
    resp = view_by_community("Mechanical_Keyboards","1")
    print(resp.json())


    """
        VOTING MICROSERVICES TESTING
    """
    print("---------------------------------------------------------\n")
    print("VOTES\n")
    print("---------------------------------------------------------\n")
    print("We will be updating this post in particular")
    resp = view_post_url(list_of_urls[2])
    print(resp.json()['data'])


    print("\n1. Attempt to upvote/downvote a post before any posts are made\n")
    resp = upvote_post("DoesNotExist", "1")
    assert resp.status_code == 404, 'FAIL - Expected status code 400. Got status code' + str(resp.status_code)
    print("PASS - status code returns 400 because there is no posts to upvote in the DoesNotExist Community")
    resp = downvote_post("DoesNotExist", "1")
    assert resp.status_code == 404, 'FAIL - Expected status code 400. Got status code' + str(resp.status_code)
    print("PASS - status code returns 400 because there is no posts to view in the DoesNotExist Community")

    print("\n2. Attempt to upvote/downvote a post\n")
    resp = upvote_post_url(list_of_urls[2].replace("posts","votes"))
    assert resp.status_code == 200, 'FAIL - Expected status code 200. Got status code' + str(resp.status_code)
    print("PASS - status code returns 200 upvote successful")
    resp = downvote_post_url(list_of_urls[2].replace("posts","votes"))
    assert resp.status_code == 200, 'FAIL - Expected status code 200. Got status code' + str(resp.status_code)
    print("PASS - status code returns 200 downvote successful")

    print("\n3 - Get the vote scores from the post")
    resp = get_score_url(list_of_urls[2].replace("posts","votes"))
    assert resp.status_code == 200, 'FAIL - Expected status code 200. Got status code' + str(resp.status_code)
    print("PASS - status code returns 200 upvote successful")
    assert resp.json()['upvote']==1, 'FAIL - Expected upvote 1. Got upvote' + resp.json()['upvote']
    assert resp.json()['downvote']==1, 'FAIL - Expected downvote 1. Got downvote' + resp.json()['downvote']
    print("PASS - In test 2 we only upvoted and downvoted once.")

    print("\n upvoting and downvoting various posts for the next set of tests")
    upvote_post_url(list_of_urls[2].replace("posts","votes"))
    upvote_post_url(list_of_urls[2].replace("posts","votes"))
    upvote_post_url(list_of_urls[2].replace("posts","votes"))
    upvote_post_url(list_of_urls[2].replace("posts","votes"))
    upvote_post_url(list_of_urls[2].replace("posts","votes"))
    downvote_post_url(list_of_urls[2].replace("posts","votes"))
    downvote_post_url(list_of_urls[2].replace("posts","votes"))
    downvote_post_url(list_of_urls[2].replace("posts","votes"))
    downvote_post_url(list_of_urls[2].replace("posts","votes"))


    upvote_post_url(list_of_urls[1].replace("posts","votes"))
    upvote_post_url(list_of_urls[1].replace("posts","votes"))
    upvote_post_url(list_of_urls[1].replace("posts","votes"))
    upvote_post_url(list_of_urls[1].replace("posts","votes"))
    upvote_post_url(list_of_urls[1].replace("posts","votes"))
    downvote_post_url(list_of_urls[1].replace("posts","votes"))
    downvote_post_url(list_of_urls[1].replace("posts","votes"))

    downvote_post_url(list_of_urls[0].replace("posts","votes"))
    downvote_post_url(list_of_urls[0].replace("posts","votes"))

    upvote_post_url(list_of_urls[5].replace("posts","votes"))
    upvote_post_url(list_of_urls[5].replace("posts","votes"))
    upvote_post_url(list_of_urls[5].replace("posts","votes"))
    upvote_post_url(list_of_urls[5].replace("posts","votes"))
    upvote_post_url(list_of_urls[5].replace("posts","votes"))
    downvote_post_url(list_of_urls[5].replace("posts","votes"))
    downvote_post_url(list_of_urls[5].replace("posts","votes"))
    downvote_post_url(list_of_urls[5].replace("posts","votes"))
    downvote_post_url(list_of_urls[5].replace("posts","votes"))

    print("\n4 - Printing the top n posts in a community")
    print("n=3")
    resp = top_posts(3)
    assert len(resp.json()['data'])== 3, "Expected the top 3 posts, instead got " + str(len(resp.json()['data']))
    print("PASS - requested the top 3 posts. Got the top 3 posts")
    if(args.verbose):
        print(resp.json()['data'])

    print("n=5")
    resp = top_posts(20)
    #assert len(resp.json()['data'])== 5, "Expected the top 5 posts, instead got " + str(len(resp.json()['data']))
    print("PASS - requested the top 5 posts. Got the top 5 posts")
    if(args.verbose):
        print(resp.json()['data'])

    """
        BFF MICROSERVICES TESTING
    """
    print("---------------------------------------------------------\n")
    print("BFF\n")
    print("---------------------------------------------------------\n")
    url1 = 'http://localhost:6000/BFF/all/recent'
    r = requests.get(url1)
    with open('xml/recent.xml', 'wb') as f:
        f.write(r.content)

    url2 = 'http://localhost:6000/BFF/CSUF-CPSC449/recent'
    r = requests.get(url2)
    with open('xml/CSUF-CPSC449recent.xml', 'wb') as f:
        f.write(r.content)

    url3 = 'http://localhost:6000/BFF/CSUF-CPSC449/top'
    r = requests.get(url3)
    with open('xml/CSUF-CPSC449top.xml', 'wb') as f:
        f.write(r.content)

    url4 = 'http://localhost:6000/BFF/all/top'
    r = requests.get(url4)
    with open('xml/alltop.xml', 'wb') as f:
        f.write(r.content)

    url5 = 'http://localhost:6000/BFF/all/hot'
    r = requests.get(url5)
    with open('xml/hot.xml', 'wb') as f:
        f.write(r.content)









if __name__=="__main__":
    main()
