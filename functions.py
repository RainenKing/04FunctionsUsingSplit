def meal_time(day):
  hours, minutes = day.split(":") 

  hours = int(hours)
  minutes = int(minutes)

  timenum = hours + minutes/60

  if timenum >= 7 and timenum  <= 8:
   return "breakfast"
  elif timenum >= 12 and timenum <= 13:
   return "lunch"
  elif timenum >= 17 and timenum <= 18:
   return "dinner"

print(meal_time("7:00"))
print(meal_time("12:00"))
print(meal_time("19:00"))
print(meal_time("18:00"))



def file_name(data_file):
  file, extension = data_file.split(".")
  return extension
  
  
  
print(file_name("data.csv"))



def is_image_file(file_name):
  file_name, extension = file_name.split(".")
  if extension == "jpg" or extension == "jpeg" or extension == "png" or extension == "gif" or extension == "tiff":
    return True
  else:
    return False
    


print(is_image_file("data.csv"))
print(is_image_file("data.txt"))
print(is_image_file("data.jpeg"))
print(is_image_file("data.png"))
print(is_image_file("data.gif"))
print(is_image_file("data.tiff"))