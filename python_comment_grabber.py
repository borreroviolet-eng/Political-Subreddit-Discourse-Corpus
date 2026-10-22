import praw #reddit API wrapper
import os #navigating direcctories 
import shutil #for directory manipulation


#connects to reddit, stores to variable
DEBUG = True #bool flag for debug statements

# credentials are read from environment variables so they never live in the code
# (read-only access, so no Reddit username or password is needed)
reddit = praw.Reddit(client_id = os.environ['REDDIT_CLIENT_ID'], \
                    client_secret = os.environ['REDDIT_CLIENT_SECRET'], \
                    user_agent = os.environ['REDDIT_USER_AGENT'])

# in this sample script
# program will pull top n posts from r/Liberal, r/Conservative, 
# r/politics and r/NeutralPolitics and pull top m comments from each

num_posts_to_copy = 10
num_comms_to_copy = 1000

txt_format = '.txt'
txt_encoding = 'utf-8'

output_base_dir = 'corpus_output/' #text files are saved here, relative to where the script runs


#function will use reddit instance to access provided subreddit
#pull top n posts and copy top m comments from each
#comments will be stored in txt files organized by post

def GrabCommentsFrom(sr_name,output_dir='all_posts'):
    if DEBUG:
        print("comments being grabbed from " + sr_name)
    
    os.makedirs(output_base_dir + output_dir, exist_ok = True) #creates output folder if missing

    sub_to_copy = reddit.subreddit(sr_name)
    posts_to_copy = sub_to_copy.top(time_filter = 'all', limit = num_posts_to_copy)
    
    if DEBUG:
        print('------posts being copied------')
        for submission in posts_to_copy:
            print(submission.title)
    
    post_num = 1
    
    posts_to_copy = sub_to_copy.top(time_filter = 'all', limit = num_posts_to_copy)
    for submission in posts_to_copy:
        
        if DEBUG:
            print('\nextracting comments from post ' + submission.name)
        
        num_comms_copied = 0
        #sorts comments and opens any comment trees necessary to hit target num
        submission.comment_sort = 'top'
        submission.comments.replace_more(threshold = num_comms_to_copy)
        
        #create new file
        output_path = output_base_dir + output_dir + '/' + sr_name + '_' + str(post_num) + txt_format
        output_file = open(output_path,'w+',encoding = txt_encoding)
        
        #iterate through top comments and write them to output_file
        for comment in submission.comments.list():
            with open(output_path, 'a+', encoding = txt_encoding) as writefile:
                writefile.write('\n<' + str(num_comms_copied) + '> ' + '<' + str(comment.id) + '> ' + comment.body + '\n')
                num_comms_copied += 1
            
                if DEBUG:
                    print(str(comment.id) + ' copied to file.')
                    
            #redundancy alert: this if block is copied below for posts with less than n comments
            if(num_comms_copied >= num_comms_to_copy):
                break
                
        if DEBUG:
            print('file saved to: ' + output_path)
            if os.path.isfile(output_path):
                print('file exists. all is well')
            else:
                print('file does not exist')
                
        writefile.close()
        post_num += 1
        print('extracting comments from post ' + submission.name + ' completed \n\n')

        
    print('------------comment extraction from ' + sr_name + ' completed------------\n\n')    
    return
    

#FUNCTION CALLS WITH DESIRED SUBREDDITS

GrabCommentsFrom('Liberal')
GrabCommentsFrom('Conservative')
GrabCommentsFrom('politics')
GrabCommentsFrom('NeutralPolitics')
print('~~~~~~~~~~~~~~~~~~~~extractions completed~~~~~~~~~~~~~~~~~~~~')