path ="D:/PythonPortfolio/Projects/"
# import subprocess, sys

# # recommended way of calling pip from within the script
# def install(package):
#     subprocess.check_call([sys.executable,"-m","pip",package])
    

# install('pytube')


try:
    # importing pytube
    from pytube import YouTube
except Exception as e:
    import sys
    import subprocess
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pytube'])



from pytube import YouTube
url = input('please enter the video url: ')
target = YouTube(url,
        use_oauth=False,
        allow_oauth_cache=True)

target.streams.get_highest_resolution().download(path)
