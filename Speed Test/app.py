import speedtest

st = speedtest.Speedtest()

try:
    print("Please wait...")
    down_speed = st.download()
    up_speed = st.upload()
except:
    print("Error")


print("Download speed: ", down_speed)
print("Upload speed: ", up_speed)