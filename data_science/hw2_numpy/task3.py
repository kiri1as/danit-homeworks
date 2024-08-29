from PIL import Image
import numpy as np

if __name__ == "__main__":
    img = Image.open('dd_gaming__gasuebmhf1iu_large.jpg')

    rgb_arr = np.array(img)
    rgb_arr_size = rgb_arr.shape
    rgb_arr_data_type = rgb_arr.dtype

    red_channel = rgb_arr[:, :, :1]
    green_channel = rgb_arr[:, :, 1:2]
    blue_channel = rgb_arr[:, :, 2:]

    red_max_val = np.max(red_channel)
    red_min_val = np.min(red_channel)
    red_avg_val = np.mean(red_channel)

    green_max_val = np.max(green_channel)
    green_min_val = np.min(green_channel)
    green_avg_val = np.mean(green_channel)

    blue_max_val = np.max(blue_channel)
    blue_min_val = np.min(blue_channel)
    blue_avg_val = np.mean(blue_channel)

    red_intensity = np.sum(red_channel)
    green_intensity = np.sum(green_channel)
    blue_intensity = np.sum(blue_channel)

    MAX_INTENSITY_RGB = np.max(np.array([red_max_val, green_max_val, blue_max_val]))
    normalized_image = rgb_arr / MAX_INTENSITY_RGB

    print(f'\nRGB array size: {rgb_arr_size}')
    print(f'RGB array data type: {rgb_arr_data_type}')

    print(f'\nRED max: {red_max_val}')
    print(f'RED min: {red_min_val}')
    print(f'RED avg: {red_avg_val}')

    print(f'\nGREEN max: {green_max_val}')
    print(f'GREEN min: {green_min_val}')
    print(f'GREEN avg: {green_avg_val}')

    print(f'\nBLUE max: {blue_max_val}')
    print(f'BLUE min: {blue_min_val}')
    print(f'BLUE avg: {blue_avg_val}')

    print(f'\nRED intensity: {red_intensity}')
    print(f'GREEN intensity: {green_intensity}')
    print(f'BLUE intensity: {blue_intensity}')

    print(f'\nMAX CHANNEL INTENSITY: {MAX_INTENSITY_RGB}')
    print(f'\nNormalized pixels: \n{normalized_image}')
