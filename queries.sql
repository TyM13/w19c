insert into client (username, joined_on, password) values
('user_one', '2020-01-01', 'pass_one'),
('user_two', '2020-02-01', 'pass_two'),
('user_three', '2020-03-01', 'pass_three');

insert into post  (client_id, content, title) values
(1, 'content_one', 'title_one'),
(2, 'content_two', 'title_two'),
(3, 'content_three', 'title_three'),
(2, 'content_four', 'title_four'),
(1, 'content_five', 'title_five');

CREATE PROCEDURE w19c.blog_post(title_input varchar(100), content_input varchar(255))
modifies sql data
begin
	insert into post (title, content)
	values (title_input, content_input)
commit