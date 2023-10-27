import time
from plyer import notification
 
 
if __name__=="__main__":
 
        notification.notify(
            title = "HEADING HERE",
            message=" DESCRIPTION HERE",
            app_icon ="D:\\Python\Project\\notification\\king.ico",
            
           
            # displaying time
            timeout=5
)
        # waiting time
        time.sleep(10)
    