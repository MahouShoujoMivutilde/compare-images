import subprocess 
import argparse
import re

def get_ssim(ref_img, cmp_img):
    p = subprocess.Popen(['ffmpeg.exe', '-loglevel', 'error', '-i', ref_img, '-i', cmp_img, '-filter_complex', 'ssim=stats_file=-', '-f', 'null', '-'], stdout = subprocess.PIPE, stderr = subprocess.PIPE)
    p.wait()
    outs, _ = p.communicate()
    return float(re.search(r'\bAll:(\d+(?:\.\d+)?)\s', outs.decode('utf-8')).group(0)[4:])

def get_args():
    parser = argparse.ArgumentParser(description = "С помощью ffmpeg рассчитывает ssim двух изображений") 
    requiredNamed = parser.add_argument_group('required named arguments')
    requiredNamed.add_argument("-ref", required = True, help = "Путь к файлу-образцу")
    requiredNamed.add_argument("-c", required = True, help = "Путь к файлу, что будет сравниваться с образцом")
    return parser.parse_args()

if __name__ == '__main__':
    args = vars(get_args())
    print('SSIM: {}'.format(get_ssim(args['ref'], args['c'])))