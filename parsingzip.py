import datetime
import pandas as pd
import zipfile, io
    
def parsing_zip_file(day, month, year):
    everything = []
    if len(str(day)) < 2:
        day = '0' + str(day)
    month_to_num = {'January': '01', 'February': '02', 'March': '03', 'April': '04', 'May': '05', 'June': '06', 'July': '07', 'August': '08', 'September': '09', 'October': '10', 'November': '11', 'December': '12'}
    num_to_month = {'1' : 'January', '2' : 'February', '3' : 'March', '4' : 'April', '5' : 'May', '6' : 'June', '7' : 'July', '8' : 'August', '9' : 'September', '10' : 'October', '11' : 'November', '12' : 'December'}
    fname = "Moonmoon chatlog/" + num_to_month[str(month)] + ' ' + str(year) + "/" + str(year) + '-' + month_to_num[num_to_month[str(month)]] + '-' + str(day) + '.txt'
    #print(fname)
    with zipfile.ZipFile("Moonmoon_chatlog.zip") as z:
        for filename in z.namelist():
            if fname == filename:
                with z.open(fname) as readfile:
                    for line in io.TextIOWrapper(readfile, 'Latin-1'):
                        info = parsing_line(repr(line))
                        everything.append(info)
    return pd.DataFrame(data = everything, columns = ['Date', 'Name', 'Message'])
    
def parsing_line(i):
    num = findnth(i, ":", 2)
    info = i[0:num+1].replace("[", "").strip().split()
    date_str = info[0].replace("-", "").replace("'", "").replace('"', "")
    time = info[1].replace(":", "")
    username = info[3].replace(":", "")
    message = i[num+2:].replace("\\n'", "").strip()
    datetime_obj = datetime.datetime(int(date_str[0:4]),int(date_str[4:6]), int(date_str[6:]), int(time[0:2]), int(time[2:4]), int(time[4:6]))
    return [datetime_obj, username, message]
    
def findnth(string, substring, n):
    parts = string.split(substring, n + 1)
    if len(parts) <= n + 1:
        return -1
    return len(string) - len(parts[-1]) - len(substring)

'''
def main():
    lol = parsing_zip_file(9, 4, 2017)
    print(lol)
    
if __name__ == '__main__':
    main()
'''