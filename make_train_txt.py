import argparse, os

parser = argparse.ArgumentParser()
parser.add_argument("--preprocessed_root", help="Root folder of the preprocessed dataset", required=True)

args = parser.parse_args()


def main(args):
    dirs = []
    for foldername in os.listdir(args.preprocessed_root):
        subdir = os.path.join(args.preprocessed_root, foldername)
        if os.path.isdir(subdir):
            for subfoldername in os.listdir(subdir):
                _subfoldername = os.path.join(subdir, subfoldername)
                if os.path.exists(os.path.join(_subfoldername, "audio.wav")):
                    dirs.append(os.path.join(subdir, subfoldername))
                else:
                    print(subfoldername + " not audio")

    content = '\n'.join(str(i) for i in dirs)
    train = open('./filelists/train.txt','w')
    val = open('./filelists/val.txt','w')
    test = open('./filelists/test.txt','w')
    train.write(content)
    val.write(content)
    test.write(content)
    train.close()
    val.close()
    test.close()

if __name__ == '__main__':
    main(args)

