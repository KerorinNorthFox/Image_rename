import glob, os, click, itertools

@click.command()
@click.argument('path', nargs=1)
def main(path):
    image_pathes = []
    image_pathes.append(glob.glob(path + '\\*.jpg'))
    image_pathes.append(glob.glob(path + '\\*.jpeg'))
    image_pathes.append(glob.glob(path + '\\*.png'))
    image_pathes.append(glob.glob(path + '\\*.gif'))
    image_pathes.append(glob.glob(path + '\\*.tiff'))
    image_pathes.append(glob.glob(path + '\\*.webp'))
    image_pathes.append(glob.glob(path + '\\*.jfif'))
    image_pathes.append(glob.glob(path + '\\*.tif'))
    image_pathes.append(glob.glob(path + '\\*.mp4'))
    image_path = list(itertools.chain.from_iterable(image_pathes))
    print(path)
    print(image_path)
    if len(image_path) == 0: return
    for x in range(len(image_path)):
        path_ext = os.path.splitext(image_path[x])
        os.rename(image_path[x], path+'\\'+str(x+1)+path_ext[1])

if __name__ == '__main__':
    main()
