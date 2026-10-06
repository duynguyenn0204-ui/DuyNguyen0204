# Mở file songs.txt để đọc
with open("songs.txt", "r", encoding="utf-8") as file:

    # Đọc tất cả các dòng
    songs = file.readlines()


# Danh sách chứa các bài hát không trùng
unique_songs = []


# Duyệt từng bài hát
for song in songs:

    # Xóa khoảng trắng và ký tự xuống dòng
    song = song.strip()

    # Nếu bài hát chưa tồn tại
    if song not in unique_songs:

        # Thêm vào danh sách
        unique_songs.append(song)


# Tạo file mới
with open("new_songs.txt", "w", encoding="utf-8") as file:

    # Ghi từng bài hát vào file
    for song in unique_songs:
        file.write(song + "\n")


print("Đã tạo file new_songs.txt")