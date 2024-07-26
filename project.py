from PIL import Image

file_name = "paddu.jpg"

with Image.open("chars.png") as img:
    size = 26.389473684210526315789473684211
    img = img.convert("L")
    densities_arr = []
    for i in range(0, 95):
        temp_img = img.crop((round(size*i), 0, round((i+1)*size), 48))
        width, height = temp_img.size
        area = width * height
        count = 0
        for y in range(height):
            for x in range(width):
                if temp_img.getpixel((x, y)) != 0:
                    count+=1
        densities_arr.append(count/area)
    maxi =max(densities_arr)
    densities_arr = [(round((x/maxi), 3)) for x in densities_arr]
    data_dict = {}
    for i in range(95):
        data_dict[densities_arr[i]] = chr(32+i)
    densities = sorted(list(data_dict.keys()))
    data_dict = {x:data_dict[x] for x in densities}

target_densities=[]
global target_dimensions
with Image.open(file_name) as img:
    img = img.convert("L")
    target_dimensions = img.size
    width, height = img.size
    for y in range(height):
        for x in range(width):
            target_densities.append(img.getpixel((x, y)))
    maxi = max(target_densities)
    target_densities=[round(x/maxi, 3) for x in target_densities]



n = len(densities)
matches = []
for target_density in target_densities:
    ans = -1
    s = 0
    e = n-1
    while s <= e:
        mid = s+(e-s)//2
        if densities[mid] == target_density:
            ans = mid
            break
        elif densities[mid] > target_density:
            e = mid-1
        else:
            s = mid+1
    if ans==-1:
        ans = mid
    matches.append((target_density, data_dict[densities[ans]]))

with open(f"{file_name.split(".")[0]}.txt", "w") as file:
    width, height = target_dimensions[0], target_dimensions[1]
    for row in range(height):
        for _ in range(row*width, (row+1)*width):
            file.write(matches[_][1])
        file.write("\n")