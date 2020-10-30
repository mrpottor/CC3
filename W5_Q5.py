#  minute hand moves 6 degrees in a minute

def calcAngle(h,m):
		if (h < 0 or m < 0 or h > 12 or m > 60):
			print('Wrong input')
		
		if (h == 12):
			h = 0
		if (m == 60):
			m = 0
			h += 1;
			if(h>12):
				h = h-12;
		
		hour_angle = 0.5 * (h * 60 + m)
		minute_angle = 6 * m
		
		angle = abs(hour_angle - minute_angle)

		angle = min(360 - angle, angle)
		
		return angle

def main():
    h,m,t = list(map(int, input('H,M,T saperated with spaces:-').split()))
    for i in range(t):
        mi = int(input('no of minutes passed:-'))
        currrent_time = mi+m
        if currrent_time >= 60:
            h +=1
            m = currrent_time - 60
        print(calcAngle(h,m))

if __name__ == '__main__':
    main()