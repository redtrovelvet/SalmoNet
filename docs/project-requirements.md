# Project Plan

## User Stories Completion

### Profile Class

* username (primary key)
* profile (1 - 1 relationship to username)
* 1 - many relationship with
  * posts
  * comments
  * likes
* many - many relationship with
  * follower
  * friend

### Post Class

* post_id (primary key) (1 - 1 relationship with username)
* username (foreign key)
* comment_id (foreign key)
* post_likes_id (foreign key)
* picture
* text
* post_type
* post_visibility (public/unlisted/friends-only)

### Follower Class

* username (foreign key) (can be follower/friend)
* notification_id (foreign key)

### Post_Likes Class

* post_likes_id (primary key) (1 - 1 relationship with post)
* username (foreign key)
* post_id (foreign key)
* count
* date

### Comment Class

* comment_id (primary key) (1 - 1 relationship with post)
* username (foreign key)
* post_id (foreign key)
* date

### Comment_Likes Class

* comment_likes_id (primary key) (1 - 1 relationship with comment)
* username (foreign key)
* comment_id (foreign key)
* count
* date

### Stream Class

* post_id (foreign key) (can be unlisted/followers-only/public)
* username (foreign key)
* post_type
* sender (foreign key) (can be follower/friend/public)

### Inbox Class

* notification_id (primary key)
* post_id (foreign key)
* post_likes_id (foreign key)
* comment_id (foreign key)
* comment_likes_id (foreign key)
* username (foreign key)
* post_type
* sender (foreign key) (can be follower/friend/public)
* date
