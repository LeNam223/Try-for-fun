import webbrowser

class Video:
	def __init__(self, title, link):
		self.title = title
		self.link = link

	def open(self):
		webbrowser.open(self.link)

class Playlist:
	def __init__(self, name, description, rating, videos):
		self.name = name
		self.description = description
		self.rating = rating
		self.videos = videos

def read_video():
	title = input("Enter title: ") + "\n"
	link = input("Enter link: ") + "\n"
	video = Video(title, link)
	return video

def read_videos():
	videos = []
	total_video = input("Enter how many videos: ")
	for i in range(int(total_video)):
		print("Enter video ", i+1)
		vid = read_video()
		videos.append(vid)
	return videos

def print_video(video):
	print("Video title: ", video.title, end="")
	print("Video link: ", video.link, end="")

def print_videos(videos):
	for i in range(len(videos)):
		print_video(videos[i])

def write_videos_to_txt(videos, file):
	total = len(videos)
	file.write(str(total) + "\n")
	for i in range(total):
		file.write(videos[i].title)
		file.write(videos[i].link)

def read_videos_from_txt(file):
	videos = []
	total = file.readline()
	for i in range(int(total)):
		title = file.readline()
		link = file.readline()
		video = Video(title, link)
		videos.append(video)
	return videos

def read_playlist():
	playlist_name = input("Enter playlist name: ") + "\n"
	playlist_description = input("Enter playlist description: ") + "\n"
	playlist_rating = input("Enter playlist rating (1-5): ") + "\n"
	playlist_videos = read_videos()
	playlist = Playlist(playlist_name, playlist_description, playlist_rating, playlist_videos)
	print("\nCreat playlist succeedfully !!!")
	return playlist

def write_playlist_to_txt(playlist):
	with open("data.txt", "w") as file:
		file.write(playlist.name)
		file.write(playlist.description)
		file.write(playlist.rating)
		write_videos_to_txt(playlist.videos, file)

def read_playlist_from_txt():
	with open("data.txt", "r") as file:
		playlist_name = file.readline()
		playlist_description = file.readline()
		playlist_rating = file.readline()
		playlist_videos = read_videos_from_txt(file)
	playlist = Playlist(playlist_name, playlist_description, playlist_rating, playlist_videos)
	return playlist

def print_playlist(playlist):
	print("-----------")
	print("Playlist name: " + playlist.name, end="")
	print("Playlist description: " + playlist.description, end="")
	print("Playlist rating: " + playlist.rating, end="")
	print_videos(playlist.videos)

def show_menu():
	print("|---------Main Menu--------|")
	print("|--------------------------|")
	print("| Option 1: Creat playlist |")
	print("| Option 2: Show playlist  |")
	print("| Option 3: Play a video   |")
	print("| Option 4: Add a video    |")
	print("| Option 5: Remove a video |")
	print("| Option 6: Search a video |")
	print("| Option 7: Update playlist|")
	print("| Option 8: Save and exit  |")
	print("|--------------------------|")

def select_in_range(propmt, min, max):
	choice = input(propmt)
	while not choice.isdigit():
		choice = input(propmt)
	
	choice = int(choice)
	if choice < min or choice > max:
		choice = input(propmt)
	else:
		return choice

def play_video(playlist):
	for i in range(len(playlist.videos)):
		print("Video " + str(i+1) + ":")
		print_video(playlist.videos[i])
	choice = select_in_range("Select video want to play (1-{0}): ".format(len(playlist.videos)), 1, len(playlist.videos))
	playlist.videos[choice-1].open()

def add_video(playlist):
	print("\nEnter new video information: ")
	new_video_title = input("Enter new video title: ") + "\n"
	new_video_link = input("Enter new video link: ") + "\n"
	new_video = Video(new_video_title, new_video_link)
	playlist.videos.append(new_video)

def remove_video(playlist):
	print_videos(playlist.videos)
	choice = select_in_range("Select video want to delete (1-{0}): ".format(len(playlist.videos)), 1, len(playlist.videos))
	del playlist.videos[choice-1]

def	search_video_by_name(playlist):
	video_search = input("Enter name of video want to search: ")
	video_found = []
	for i in range(len(playlist.videos)):
		if video_search in playlist.videos[i].title.lower():
			video_found.append(playlist.videos[i])
	
	total_video_found = len(video_found)
	if total_video_found == 0:
		print("Video not found")
	elif total_video_found == 1:
		print("1 video found")
		print("-----------")
		print_videos(video_found)
	else:
		print("{0} videos found".format(total_video_found))
		print("-----------")
		for i in range(total_video_found):
			print("Video " + str(i+1) + ":")
			print_video(video_found[i])

def update_playlist(playlist):
	print("Update playlist?")
	print("1. Name")
	print("2. Description")	
	print("3. Rating")

	choice = select_in_range("Enter what you want to update (1-3):", 1, 3)
	if choice == 1:
		new_playlist_name = input("Enter new name for playlist: ") + "\n"
		playlist.name = new_playlist_name
		print("Updated Successfully !!!")
		return playlist
	if choice == 2:
		new_playlist_description = input("Enter new description for playlist: ") + "\n"
		playlist.description = new_playlist_description
		print("Updated Successfully !!!")
		return playlist
	if choice == 3:
		new_playlist_rating = str(select_in_range("Enter new rating (1-5): ",1, 5)) + "\n"
		playlist.rating = new_playlist_rating
		print("Updated Successfully !!!")
		return playlist

def main():
	try:
		playlist = read_playlist_from_txt()
		print("Loaded data succeedfully !!!")
	except:
		print("Welcome the first user !!!")

	while True:
		show_menu()
		choice = select_in_range("Select an Option(1-8): ", 1, 8)
		if choice == 1:
			playlist = read_playlist()
			input("\nEnter to show Main Menu.\n")
		elif choice == 2:
			print_playlist(playlist)
			input("\nEnter to show Main Menu.\n")
		elif choice == 3:
			play_video(playlist)
			input("\nEnter to show Main Menu.\n")
		elif choice == 4:
			add_video(playlist)
			input("\nEnter to show Main Menu.\n")
		elif choice == 5:
			remove_video(playlist)
			input("\nEnter to show Main Menu.\n")
		elif choice == 6:
			search_video_by_name(playlist)
			input("\nEnter to show Main Menu.\n")
		elif choice == 7:
			update_playlist(playlist)
			int("\nEnter to show Main Menu.\n")
		elif choice == 8:
			write_playlist_to_txt(playlist)
			break

main()
