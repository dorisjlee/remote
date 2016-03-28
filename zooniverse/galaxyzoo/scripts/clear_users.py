

for user in User.objects.all():
	if user.get_username() == "admin":
		continue;
	user.delete()