# # App Users II

# Wow!  Literally overnight, your \<INSERT APPLICATION NAME\> app has really taken off!  You decide to add a new feature to your app: posts.

# In order to gain this new functionality, you'll have to modify your original `User` class.

# ## Requirements

# 1. Add a method to your `User` class that allows for creating a new user post.
# 2. Add any necessary instance properties to make step 1 work.  What data structure should you use?
# 3. Add a class variable that stores the posts from every user.  What data structure should you use?
# 4. Make sure that the the information stays in sync!

# ## Bonus

# Add a method that allows for deleting a post.  Again, make sure that your information stays in sync.

# your improved User class goes here

class User:
    all_posts = []

    def __init__(self, username):
        self.username = username
        self.posts = []

    def create_post(self, content):
        post = {
            "username": self.username,
            "content": content
        }
        self.posts.append(post)
        User.all_posts.append(post)
        return post

    def delete_post(self, post):
        if post in self.posts:
            self.posts.remove(post)
            User.all_posts.remove(post)
            return post
        return None
    def view_all_posts(self):
        return self.posts

    @classmethod
    def view_all_user_posts(cls):
        return cls.all_posts

    @classmethod
    def delete_user_post(cls, post):
        if post in cls.all_posts:
            cls.all_posts.remove(post)
            # Also remove from the user's individual posts
            for user in cls.__subclasses__():
                for instance in user.__dict__.values():
                    if isinstance(instance, User) and post in instance.posts:
                        instance.posts.remove(post)
            return post
        return None