import novation_launchpad as lpd
import time

def main():

	lp = lpd.LaunchKeyMini()

	if lp.Open( 0, "mk2" ):
		print( " - Launchpad Mk2: OK" )
	else:
		print( " - Launchpad Mk2: ERROR" )
		return

	lp.ButtonFlush()

	lp.LedAllOn(5)
	time.sleep(1)

	lp.Reset()
	lp.Close()
	
if __name__ == '__main__':
	main()
