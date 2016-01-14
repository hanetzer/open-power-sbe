import sys
sys.path.append("targets/p9_nimbus/sbeTest" )
import testUtil
err = False
#from testWrite import *


PUTSCOM_TESTDATA = [0,0,0,6,
                    0,0,0xA2,0x02,
                    0,0,0x0,0x00,
                    0,0x05,0x00,0x3E, #scratch reg 7 (32-bit)
                    0x00,0xff,0x00,0xff,
                    0x00,0x00,0x00,0x00 ]

PUTSCOM_EXPDATA = [0xc0,0xde,0xa2,0x02,
                   0x0,0x0,0x0,0x0,
                   0x00,0x0,0x0,0x03];


MODIFYSCOM_TESTDATA = [0,0,0,7,
            0,0,0xA2,0x03,
            0,0,0x0,0x01,
            0,0,0x0,0x00,
            0,0x05,0x00,0x3E,
            0xde,0x00,0xff,0x00,
            0x00,0x00,0x00,0x00]

MODIFYSCOM_EXPDATA = [0xc0,0xde,0xa2,0x03,
                   0x0,0x0,0x0,0x0,
                   0x00,0x0,0x0,0x03];

GETSCOM4MODIFYSCOM_TESTDATA = [0,0,0,4,
                   0,0,0xA2,0x01,
                   0,0,0x0,0x00,
                   0,0x05,0x0,0x3E]

GETSCOM4MODIFYSCOM_EXPDATA = [0xde,0xff,0xff,0xff,
                   0x00,0x00,0x00,0x00,
                   0xc0,0xde,0xa2,0x01,
                   0x0,0x0,0x0,0x0,
                   0x00,0x0,0x0,0x03];

# MAIN Test Run Starts Here...
#-------------------------------------------------
def main( ):
    testUtil.runCycles( 10000000 )

    testUtil.writeUsFifo( PUTSCOM_TESTDATA )
    testUtil.writeEot( )
    testUtil.readDsFifo( PUTSCOM_EXPDATA )
    testUtil.readEot( )

    testUtil.writeUsFifo( MODIFYSCOM_TESTDATA )
    testUtil.writeEot( )
    testUtil.readDsFifo( MODIFYSCOM_EXPDATA )
    testUtil.readEot( )

    testUtil.writeUsFifo( GETSCOM4MODIFYSCOM_TESTDATA )
    testUtil.writeEot( )
    testUtil.readDsFifo( GETSCOM4MODIFYSCOM_EXPDATA )
    testUtil.readEot( )

#-------------------------------------------------
# Calling all test code
#-------------------------------------------------
main()

if err:
    print ("\nTest Suite completed with error(s)")
    #sys.exit(1)
else:
    print ("\nTest Suite completed with no errors")
    #sys.exit(0);

