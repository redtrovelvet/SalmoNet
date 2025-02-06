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

* post_id (primary key)
* comment_id (foreign key)
* post_likes_id (foreign key)
* picture
* posted (boolean)

### Follower Class

* username (foreign key) ( can be follower/friend)
* notification_id (foreign key)

### Post_Likes Class

* post_likes_id (primary key)
* username (foreign key)
* post_id (foreign key)
* count
* date

### Comment Class

* comment_id (primary key)
* username (foreign key)
* post_id (foreign key)
* date

### Stream Class

* post_id (foreign key) (can be unlisted/followers-only/public)
* username (foreign key)
* notification_type (foreign key)
* sender (foreign key) (can be follower/friend/public)

### Inbox Class

* notification_id (primary key)
* post_id (foreign key)
* username (foreign key)
* notification_type (foreign key)
* sender (foreign key) (can be follower/friend/public)
* date
