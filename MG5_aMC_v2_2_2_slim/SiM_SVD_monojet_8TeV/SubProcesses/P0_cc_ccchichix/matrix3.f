      SUBROUTINE SMATRIX3(P,ANS)
C     
C     Generated by MadGraph5_aMC@NLO v. 2.2.2, 2014-11-06
C     By the MadGraph5_aMC@NLO Development Team
C     Visit launchpad.net/madgraph5 and amcatnlo.web.cern.ch
C     
C     MadGraph5_aMC@NLO for Madevent Version
C     
C     Returns amplitude squared summed/avg over colors
C     and helicities
C     for the point in phase space P(0:3,NEXTERNAL)
C     
C     Process: c~ c~ > c~ c~ chi chi~ WEIGHTED=4
C     
      IMPLICIT NONE
C     
C     CONSTANTS
C     
      INCLUDE 'genps.inc'
      INCLUDE 'maxconfigs.inc'
      INCLUDE 'nexternal.inc'
      INCLUDE 'maxamps.inc'
      INTEGER                 NCOMB
      PARAMETER (             NCOMB=64)
      INTEGER    NGRAPHS
      PARAMETER (NGRAPHS=44)
      INTEGER    NDIAGS
      PARAMETER (NDIAGS=44)
      INTEGER    THEL
      PARAMETER (THEL=2*NCOMB)
C     
C     ARGUMENTS 
C     
      REAL*8 P(0:3,NEXTERNAL),ANS
C     
C     LOCAL VARIABLES 
C     
      INTEGER NHEL(NEXTERNAL,NCOMB),NTRY(2)
      INTEGER ISHEL(2)
      REAL*8 T,MATRIX3
      REAL*8 R,SUMHEL,TS(NCOMB)
      INTEGER I,IDEN
      INTEGER JC(NEXTERNAL),II
      LOGICAL GOODHEL(NCOMB,2)
      REAL*8 HWGT, XTOT, XTRY, XREJ, XR, YFRAC(0:NCOMB)
      INTEGER NGOOD(2), IGOOD(NCOMB,2)
      INTEGER JHEL(2), J, JJ
C     
C     GLOBAL VARIABLES
C     
      DOUBLE PRECISION AMP2(MAXAMPS), JAMP2(0:MAXFLOW)
      COMMON/TO_AMPS/  AMP2,       JAMP2

      CHARACTER*101         HEL_BUFF
      COMMON/TO_HELICITY/  HEL_BUFF

      INTEGER IMIRROR
      COMMON/TO_MIRROR/ IMIRROR

      REAL*8 POL(2)
      COMMON/TO_POLARIZATION/ POL

      INTEGER          ISUM_HEL
      LOGICAL                    MULTI_CHANNEL
      COMMON/TO_MATRIX/ISUM_HEL, MULTI_CHANNEL
      INTEGER MAPCONFIG(0:LMAXCONFIGS), ICONFIG
      COMMON/TO_MCONFIGS/MAPCONFIG, ICONFIG
      INTEGER SUBDIAG(MAXSPROC),IB(2)
      COMMON/TO_SUB_DIAG/SUBDIAG,IB
      DATA XTRY, XREJ /0,0/
      DATA NTRY /0,0/
      DATA NGOOD /0,0/
      DATA ISHEL/0,0/
      SAVE YFRAC, IGOOD, JHEL
      DATA GOODHEL/THEL*.FALSE./
      DATA (NHEL(I,   1),I=1,6) /-1,-1,-1,-1,-1,-1/
      DATA (NHEL(I,   2),I=1,6) /-1,-1,-1,-1,-1, 1/
      DATA (NHEL(I,   3),I=1,6) /-1,-1,-1,-1, 1,-1/
      DATA (NHEL(I,   4),I=1,6) /-1,-1,-1,-1, 1, 1/
      DATA (NHEL(I,   5),I=1,6) /-1,-1,-1, 1,-1,-1/
      DATA (NHEL(I,   6),I=1,6) /-1,-1,-1, 1,-1, 1/
      DATA (NHEL(I,   7),I=1,6) /-1,-1,-1, 1, 1,-1/
      DATA (NHEL(I,   8),I=1,6) /-1,-1,-1, 1, 1, 1/
      DATA (NHEL(I,   9),I=1,6) /-1,-1, 1,-1,-1,-1/
      DATA (NHEL(I,  10),I=1,6) /-1,-1, 1,-1,-1, 1/
      DATA (NHEL(I,  11),I=1,6) /-1,-1, 1,-1, 1,-1/
      DATA (NHEL(I,  12),I=1,6) /-1,-1, 1,-1, 1, 1/
      DATA (NHEL(I,  13),I=1,6) /-1,-1, 1, 1,-1,-1/
      DATA (NHEL(I,  14),I=1,6) /-1,-1, 1, 1,-1, 1/
      DATA (NHEL(I,  15),I=1,6) /-1,-1, 1, 1, 1,-1/
      DATA (NHEL(I,  16),I=1,6) /-1,-1, 1, 1, 1, 1/
      DATA (NHEL(I,  17),I=1,6) /-1, 1,-1,-1,-1,-1/
      DATA (NHEL(I,  18),I=1,6) /-1, 1,-1,-1,-1, 1/
      DATA (NHEL(I,  19),I=1,6) /-1, 1,-1,-1, 1,-1/
      DATA (NHEL(I,  20),I=1,6) /-1, 1,-1,-1, 1, 1/
      DATA (NHEL(I,  21),I=1,6) /-1, 1,-1, 1,-1,-1/
      DATA (NHEL(I,  22),I=1,6) /-1, 1,-1, 1,-1, 1/
      DATA (NHEL(I,  23),I=1,6) /-1, 1,-1, 1, 1,-1/
      DATA (NHEL(I,  24),I=1,6) /-1, 1,-1, 1, 1, 1/
      DATA (NHEL(I,  25),I=1,6) /-1, 1, 1,-1,-1,-1/
      DATA (NHEL(I,  26),I=1,6) /-1, 1, 1,-1,-1, 1/
      DATA (NHEL(I,  27),I=1,6) /-1, 1, 1,-1, 1,-1/
      DATA (NHEL(I,  28),I=1,6) /-1, 1, 1,-1, 1, 1/
      DATA (NHEL(I,  29),I=1,6) /-1, 1, 1, 1,-1,-1/
      DATA (NHEL(I,  30),I=1,6) /-1, 1, 1, 1,-1, 1/
      DATA (NHEL(I,  31),I=1,6) /-1, 1, 1, 1, 1,-1/
      DATA (NHEL(I,  32),I=1,6) /-1, 1, 1, 1, 1, 1/
      DATA (NHEL(I,  33),I=1,6) / 1,-1,-1,-1,-1,-1/
      DATA (NHEL(I,  34),I=1,6) / 1,-1,-1,-1,-1, 1/
      DATA (NHEL(I,  35),I=1,6) / 1,-1,-1,-1, 1,-1/
      DATA (NHEL(I,  36),I=1,6) / 1,-1,-1,-1, 1, 1/
      DATA (NHEL(I,  37),I=1,6) / 1,-1,-1, 1,-1,-1/
      DATA (NHEL(I,  38),I=1,6) / 1,-1,-1, 1,-1, 1/
      DATA (NHEL(I,  39),I=1,6) / 1,-1,-1, 1, 1,-1/
      DATA (NHEL(I,  40),I=1,6) / 1,-1,-1, 1, 1, 1/
      DATA (NHEL(I,  41),I=1,6) / 1,-1, 1,-1,-1,-1/
      DATA (NHEL(I,  42),I=1,6) / 1,-1, 1,-1,-1, 1/
      DATA (NHEL(I,  43),I=1,6) / 1,-1, 1,-1, 1,-1/
      DATA (NHEL(I,  44),I=1,6) / 1,-1, 1,-1, 1, 1/
      DATA (NHEL(I,  45),I=1,6) / 1,-1, 1, 1,-1,-1/
      DATA (NHEL(I,  46),I=1,6) / 1,-1, 1, 1,-1, 1/
      DATA (NHEL(I,  47),I=1,6) / 1,-1, 1, 1, 1,-1/
      DATA (NHEL(I,  48),I=1,6) / 1,-1, 1, 1, 1, 1/
      DATA (NHEL(I,  49),I=1,6) / 1, 1,-1,-1,-1,-1/
      DATA (NHEL(I,  50),I=1,6) / 1, 1,-1,-1,-1, 1/
      DATA (NHEL(I,  51),I=1,6) / 1, 1,-1,-1, 1,-1/
      DATA (NHEL(I,  52),I=1,6) / 1, 1,-1,-1, 1, 1/
      DATA (NHEL(I,  53),I=1,6) / 1, 1,-1, 1,-1,-1/
      DATA (NHEL(I,  54),I=1,6) / 1, 1,-1, 1,-1, 1/
      DATA (NHEL(I,  55),I=1,6) / 1, 1,-1, 1, 1,-1/
      DATA (NHEL(I,  56),I=1,6) / 1, 1,-1, 1, 1, 1/
      DATA (NHEL(I,  57),I=1,6) / 1, 1, 1,-1,-1,-1/
      DATA (NHEL(I,  58),I=1,6) / 1, 1, 1,-1,-1, 1/
      DATA (NHEL(I,  59),I=1,6) / 1, 1, 1,-1, 1,-1/
      DATA (NHEL(I,  60),I=1,6) / 1, 1, 1,-1, 1, 1/
      DATA (NHEL(I,  61),I=1,6) / 1, 1, 1, 1,-1,-1/
      DATA (NHEL(I,  62),I=1,6) / 1, 1, 1, 1,-1, 1/
      DATA (NHEL(I,  63),I=1,6) / 1, 1, 1, 1, 1,-1/
      DATA (NHEL(I,  64),I=1,6) / 1, 1, 1, 1, 1, 1/
      DATA IDEN/72/
C     ----------
C     BEGIN CODE
C     ----------
      NTRY(IMIRROR)=NTRY(IMIRROR)+1
      DO I=1,NEXTERNAL
        JC(I) = +1
      ENDDO

      IF (MULTI_CHANNEL) THEN
        DO I=1,NDIAGS
          AMP2(I)=0D0
        ENDDO
        JAMP2(0)=2
        DO I=1,INT(JAMP2(0))
          JAMP2(I)=0D0
        ENDDO
      ENDIF
      ANS = 0D0
      WRITE(HEL_BUFF,'(20I5)') (0,I=1,NEXTERNAL)
      DO I=1,NCOMB
        TS(I)=0D0
      ENDDO
      IF (ISHEL(IMIRROR) .EQ. 0 .OR. NTRY(IMIRROR) .LE. MAXTRIES) THEN
        DO I=1,NCOMB
          IF (GOODHEL(I,IMIRROR) .OR. NTRY(IMIRROR).LE.MAXTRIES) THEN
            T=MATRIX3(P ,NHEL(1,I),JC(1))
            DO JJ=1,NINCOMING
              IF(POL(JJ).NE.1D0.AND.NHEL(JJ,I).EQ.INT(SIGN(1D0
     $         ,POL(JJ)))) THEN
                T=T*ABS(POL(JJ))
              ELSE IF(POL(JJ).NE.1D0)THEN
                T=T*(2D0-ABS(POL(JJ)))
              ENDIF
            ENDDO
            ANS=ANS+DABS(T)
            TS(I)=T
          ENDIF
        ENDDO
        JHEL(IMIRROR) = 1
        IF(NTRY(IMIRROR).LE.MAXTRIES)THEN
          DO I=1,NCOMB
            IF (.NOT.GOODHEL(I,IMIRROR) .AND. (DABS(TS(I)).GT.ANS
     $       *LIMHEL/NCOMB)) THEN
              GOODHEL(I,IMIRROR)=.TRUE.
              NGOOD(IMIRROR) = NGOOD(IMIRROR) +1
              IGOOD(NGOOD(IMIRROR),IMIRROR) = I
              PRINT *,'Added good helicity ',I,TS(I)*NCOMB/ANS
     $         ,' in event ',NTRY(IMIRROR)
            ENDIF
          ENDDO
        ENDIF
        IF(NTRY(IMIRROR).EQ.MAXTRIES)THEN
          ISHEL(IMIRROR)=MIN(ISUM_HEL,NGOOD(IMIRROR))
        ENDIF
      ELSE  !LOOP OVER GOOD HELICITIES
        DO J=1,ISHEL(IMIRROR)
          JHEL(IMIRROR)=JHEL(IMIRROR)+1
          IF (JHEL(IMIRROR) .GT. NGOOD(IMIRROR)) JHEL(IMIRROR)=1
          HWGT = REAL(NGOOD(IMIRROR))/REAL(ISHEL(IMIRROR))
          I = IGOOD(JHEL(IMIRROR),IMIRROR)
          T=MATRIX3(P ,NHEL(1,I),JC(1))
          DO JJ=1,NINCOMING
            IF(POL(JJ).NE.1D0.AND.NHEL(JJ,I).EQ.INT(SIGN(1D0,POL(JJ)))
     $       ) THEN
              T=T*ABS(POL(JJ))
            ELSE IF(POL(JJ).NE.1D0)THEN
              T=T*(2D0-ABS(POL(JJ)))
            ENDIF
          ENDDO
          ANS=ANS+DABS(T)*HWGT
          TS(I)=T*HWGT
        ENDDO
        IF (ISHEL(IMIRROR) .EQ. 1) THEN
          WRITE(HEL_BUFF,'(20i5)')(NHEL(II,I),II=1,NEXTERNAL)
C         Set right sign for ANS, based on sign of chosen helicity
          ANS=DSIGN(ANS,TS(I))
        ENDIF
      ENDIF
      IF (ISHEL(IMIRROR) .NE. 1) THEN
        CALL RANMAR(R)
        SUMHEL=0D0
        DO I=1,NCOMB
          SUMHEL=SUMHEL+DABS(TS(I))/ANS
          IF(R.LT.SUMHEL)THEN
            WRITE(HEL_BUFF,'(20i5)')(NHEL(II,I),II=1,NEXTERNAL)
C           Set right sign for ANS, based on sign of chosen helicity
            ANS=DSIGN(ANS,TS(I))
            GOTO 10
          ENDIF
        ENDDO
 10     CONTINUE
      ENDIF
      IF (MULTI_CHANNEL) THEN
        XTOT=0D0
        DO I=1,NDIAGS
          XTOT=XTOT+AMP2(I)
        ENDDO
        IF (XTOT.NE.0D0) THEN
          ANS=ANS*AMP2(SUBDIAG(3))/XTOT
        ELSE
          ANS=0D0
        ENDIF
      ENDIF
      ANS=ANS/DBLE(IDEN)
      END


      REAL*8 FUNCTION MATRIX3(P,NHEL,IC)
C     
C     Generated by MadGraph5_aMC@NLO v. 2.2.2, 2014-11-06
C     By the MadGraph5_aMC@NLO Development Team
C     Visit launchpad.net/madgraph5 and amcatnlo.web.cern.ch
C     
C     Returns amplitude squared summed/avg over colors
C     for the point with external lines W(0:6,NEXTERNAL)
C     
C     Process: c~ c~ > c~ c~ chi chi~ WEIGHTED=4
C     
      IMPLICIT NONE
C     
C     CONSTANTS
C     
      INTEGER    NGRAPHS
      PARAMETER (NGRAPHS=44)
      INCLUDE 'genps.inc'
      INCLUDE 'nexternal.inc'
      INCLUDE 'maxamps.inc'
      INTEGER    NWAVEFUNCS,     NCOLOR
      PARAMETER (NWAVEFUNCS=11, NCOLOR=2)
      REAL*8     ZERO
      PARAMETER (ZERO=0D0)
      COMPLEX*16 IMAG1
      PARAMETER (IMAG1=(0D0,1D0))
      INTEGER NAMPSO, NSQAMPSO
      PARAMETER (NAMPSO=1, NSQAMPSO=1)
      LOGICAL CHOSEN_SO_CONFIGS(NSQAMPSO)
      DATA CHOSEN_SO_CONFIGS/.TRUE./
      SAVE CHOSEN_SO_CONFIGS
C     
C     ARGUMENTS 
C     
      REAL*8 P(0:3,NEXTERNAL)
      INTEGER NHEL(NEXTERNAL), IC(NEXTERNAL)
C     
C     LOCAL VARIABLES 
C     
      INTEGER I,J,M,N
      COMPLEX*16 ZTEMP
      REAL*8 DENOM(NCOLOR), CF(NCOLOR,NCOLOR)
      COMPLEX*16 AMP(NGRAPHS), JAMP(NCOLOR,NAMPSO)
      COMPLEX*16 W(6,NWAVEFUNCS)
C     Needed for v4 models
      COMPLEX*16 DUM0,DUM1
      DATA DUM0, DUM1/(0D0, 0D0), (1D0, 0D0)/
C     
C     FUNCTION
C     
      INTEGER SQSOINDEX3
C     
C     GLOBAL VARIABLES
C     
      DOUBLE PRECISION AMP2(MAXAMPS), JAMP2(0:MAXFLOW)
      COMMON/TO_AMPS/  AMP2,       JAMP2
      INCLUDE 'coupl.inc'
C     
C     COLOR DATA
C     
      DATA DENOM(1)/1/
      DATA (CF(I,  1),I=  1,  2) /    9,    3/
C     1 T(1,3) T(2,4)
      DATA DENOM(2)/1/
      DATA (CF(I,  2),I=  1,  2) /    3,    9/
C     1 T(1,4) T(2,3)
C     ----------
C     BEGIN CODE
C     ----------
      CALL OXXXXX(P(0,1),MDL_MC,NHEL(1),-1*IC(1),W(1,1))
      CALL OXXXXX(P(0,2),MDL_MC,NHEL(2),-1*IC(2),W(1,2))
      CALL IXXXXX(P(0,3),MDL_MC,NHEL(3),-1*IC(3),W(1,3))
      CALL IXXXXX(P(0,4),MDL_MC,NHEL(4),-1*IC(4),W(1,4))
      CALL OXXXXX(P(0,5),MDL_MCHI,NHEL(5),+1*IC(5),W(1,5))
      CALL IXXXXX(P(0,6),MDL_MCHI,NHEL(6),-1*IC(6),W(1,6))
      CALL FFV6_3(W(1,3),W(1,1),GC_11,MDL_MXI,MDL_WXI,W(1,7))
      CALL FFV6_3(W(1,4),W(1,2),GC_11,MDL_MXI,MDL_WXI,W(1,8))
      CALL FFV6_1(W(1,5),W(1,7),GC_12,MDL_MCHI,ZERO,W(1,9))
C     Amplitude(s) for diagram number 1
      CALL FFV6_0(W(1,6),W(1,9),W(1,8),GC_12,AMP(1))
      CALL FFV6_2(W(1,6),W(1,7),GC_12,MDL_MCHI,ZERO,W(1,9))
C     Amplitude(s) for diagram number 2
      CALL FFV6_0(W(1,9),W(1,5),W(1,8),GC_12,AMP(2))
      CALL FFV6P0_3(W(1,3),W(1,1),GC_5,ZERO,ZERO,W(1,9))
      CALL FFV6_3(W(1,6),W(1,5),GC_12,MDL_MXI,MDL_WXI,W(1,10))
      CALL FFV6_2(W(1,4),W(1,9),GC_5,MDL_MC,ZERO,W(1,11))
C     Amplitude(s) for diagram number 3
      CALL FFV6_0(W(1,11),W(1,2),W(1,10),GC_11,AMP(3))
      CALL FFV6_1(W(1,2),W(1,9),GC_5,MDL_MC,ZERO,W(1,11))
C     Amplitude(s) for diagram number 4
      CALL FFV6_0(W(1,4),W(1,11),W(1,10),GC_11,AMP(4))
      CALL FFV6P0_3(W(1,3),W(1,1),GC_2,ZERO,ZERO,W(1,11))
      CALL FFV6_2(W(1,4),W(1,11),GC_2,MDL_MC,ZERO,W(1,9))
C     Amplitude(s) for diagram number 5
      CALL FFV6_0(W(1,9),W(1,2),W(1,10),GC_11,AMP(5))
      CALL FFV6_1(W(1,2),W(1,11),GC_2,MDL_MC,ZERO,W(1,9))
C     Amplitude(s) for diagram number 6
      CALL FFV6_0(W(1,4),W(1,9),W(1,10),GC_11,AMP(6))
      CALL FFV10_7_3(W(1,3),W(1,1),GC_31,GC_30,MDL_MZ,MDL_WZ,W(1,9))
      CALL FFV10_7_2(W(1,4),W(1,9),GC_31,GC_30,MDL_MC,ZERO,W(1,11))
C     Amplitude(s) for diagram number 7
      CALL FFV6_0(W(1,11),W(1,2),W(1,10),GC_11,AMP(7))
      CALL FFV10_7_1(W(1,2),W(1,9),GC_31,GC_30,MDL_MC,ZERO,W(1,11))
C     Amplitude(s) for diagram number 8
      CALL FFV6_0(W(1,4),W(1,11),W(1,10),GC_11,AMP(8))
      CALL FFS2_3(W(1,3),W(1,1),GC_42,MDL_MH,MDL_WH,W(1,11))
      CALL FFS2_2(W(1,4),W(1,11),GC_42,MDL_MC,ZERO,W(1,9))
C     Amplitude(s) for diagram number 9
      CALL FFV6_0(W(1,9),W(1,2),W(1,10),GC_11,AMP(9))
      CALL FFS2_1(W(1,2),W(1,11),GC_42,MDL_MC,ZERO,W(1,9))
C     Amplitude(s) for diagram number 10
      CALL FFV6_0(W(1,4),W(1,9),W(1,10),GC_11,AMP(10))
      CALL FFV6_2(W(1,4),W(1,7),GC_11,MDL_MC,ZERO,W(1,9))
C     Amplitude(s) for diagram number 11
      CALL FFV6_0(W(1,9),W(1,2),W(1,10),GC_11,AMP(11))
      CALL FFV6_1(W(1,2),W(1,7),GC_11,MDL_MC,ZERO,W(1,9))
C     Amplitude(s) for diagram number 12
      CALL FFV6_0(W(1,4),W(1,9),W(1,10),GC_11,AMP(12))
      CALL FFV6_3(W(1,3),W(1,2),GC_11,MDL_MXI,MDL_WXI,W(1,9))
      CALL FFV6_3(W(1,4),W(1,1),GC_11,MDL_MXI,MDL_WXI,W(1,7))
      CALL FFV6_1(W(1,5),W(1,9),GC_12,MDL_MCHI,ZERO,W(1,11))
C     Amplitude(s) for diagram number 13
      CALL FFV6_0(W(1,6),W(1,11),W(1,7),GC_12,AMP(13))
      CALL FFV6_2(W(1,6),W(1,9),GC_12,MDL_MCHI,ZERO,W(1,11))
C     Amplitude(s) for diagram number 14
      CALL FFV6_0(W(1,11),W(1,5),W(1,7),GC_12,AMP(14))
      CALL FFV6P0_3(W(1,3),W(1,2),GC_5,ZERO,ZERO,W(1,11))
      CALL FFV6_2(W(1,4),W(1,11),GC_5,MDL_MC,ZERO,W(1,5))
C     Amplitude(s) for diagram number 15
      CALL FFV6_0(W(1,5),W(1,1),W(1,10),GC_11,AMP(15))
      CALL FFV6_1(W(1,1),W(1,11),GC_5,MDL_MC,ZERO,W(1,5))
C     Amplitude(s) for diagram number 16
      CALL FFV6_0(W(1,4),W(1,5),W(1,10),GC_11,AMP(16))
      CALL FFV6P0_3(W(1,3),W(1,2),GC_2,ZERO,ZERO,W(1,5))
      CALL FFV6_2(W(1,4),W(1,5),GC_2,MDL_MC,ZERO,W(1,11))
C     Amplitude(s) for diagram number 17
      CALL FFV6_0(W(1,11),W(1,1),W(1,10),GC_11,AMP(17))
      CALL FFV6_1(W(1,1),W(1,5),GC_2,MDL_MC,ZERO,W(1,11))
C     Amplitude(s) for diagram number 18
      CALL FFV6_0(W(1,4),W(1,11),W(1,10),GC_11,AMP(18))
      CALL FFV10_7_3(W(1,3),W(1,2),GC_31,GC_30,MDL_MZ,MDL_WZ,W(1,11))
      CALL FFV10_7_2(W(1,4),W(1,11),GC_31,GC_30,MDL_MC,ZERO,W(1,5))
C     Amplitude(s) for diagram number 19
      CALL FFV6_0(W(1,5),W(1,1),W(1,10),GC_11,AMP(19))
      CALL FFV10_7_1(W(1,1),W(1,11),GC_31,GC_30,MDL_MC,ZERO,W(1,5))
C     Amplitude(s) for diagram number 20
      CALL FFV6_0(W(1,4),W(1,5),W(1,10),GC_11,AMP(20))
      CALL FFS2_3(W(1,3),W(1,2),GC_42,MDL_MH,MDL_WH,W(1,5))
      CALL FFS2_2(W(1,4),W(1,5),GC_42,MDL_MC,ZERO,W(1,11))
C     Amplitude(s) for diagram number 21
      CALL FFV6_0(W(1,11),W(1,1),W(1,10),GC_11,AMP(21))
      CALL FFS2_1(W(1,1),W(1,5),GC_42,MDL_MC,ZERO,W(1,11))
C     Amplitude(s) for diagram number 22
      CALL FFV6_0(W(1,4),W(1,11),W(1,10),GC_11,AMP(22))
      CALL FFV6_2(W(1,4),W(1,9),GC_11,MDL_MC,ZERO,W(1,11))
C     Amplitude(s) for diagram number 23
      CALL FFV6_0(W(1,11),W(1,1),W(1,10),GC_11,AMP(23))
      CALL FFV6_1(W(1,1),W(1,9),GC_11,MDL_MC,ZERO,W(1,11))
C     Amplitude(s) for diagram number 24
      CALL FFV6_0(W(1,4),W(1,11),W(1,10),GC_11,AMP(24))
      CALL FFV6P0_3(W(1,4),W(1,1),GC_5,ZERO,ZERO,W(1,11))
      CALL FFV6_2(W(1,3),W(1,11),GC_5,MDL_MC,ZERO,W(1,9))
C     Amplitude(s) for diagram number 25
      CALL FFV6_0(W(1,9),W(1,2),W(1,10),GC_11,AMP(25))
      CALL FFV6_2(W(1,3),W(1,10),GC_11,MDL_MC,ZERO,W(1,9))
C     Amplitude(s) for diagram number 26
      CALL FFV6_0(W(1,9),W(1,2),W(1,11),GC_5,AMP(26))
      CALL FFV6P0_3(W(1,4),W(1,1),GC_2,ZERO,ZERO,W(1,11))
      CALL FFV6_2(W(1,3),W(1,11),GC_2,MDL_MC,ZERO,W(1,5))
C     Amplitude(s) for diagram number 27
      CALL FFV6_0(W(1,5),W(1,2),W(1,10),GC_11,AMP(27))
C     Amplitude(s) for diagram number 28
      CALL FFV6_0(W(1,9),W(1,2),W(1,11),GC_2,AMP(28))
      CALL FFV10_7_3(W(1,4),W(1,1),GC_31,GC_30,MDL_MZ,MDL_WZ,W(1,11))
      CALL FFV10_7_2(W(1,3),W(1,11),GC_31,GC_30,MDL_MC,ZERO,W(1,5))
C     Amplitude(s) for diagram number 29
      CALL FFV6_0(W(1,5),W(1,2),W(1,10),GC_11,AMP(29))
C     Amplitude(s) for diagram number 30
      CALL FFV10_7_0(W(1,9),W(1,2),W(1,11),GC_31,GC_30,AMP(30))
      CALL FFS2_3(W(1,4),W(1,1),GC_42,MDL_MH,MDL_WH,W(1,11))
      CALL FFS2_2(W(1,3),W(1,11),GC_42,MDL_MC,ZERO,W(1,5))
C     Amplitude(s) for diagram number 31
      CALL FFV6_0(W(1,5),W(1,2),W(1,10),GC_11,AMP(31))
C     Amplitude(s) for diagram number 32
      CALL FFS2_0(W(1,9),W(1,2),W(1,11),GC_42,AMP(32))
      CALL FFV6_2(W(1,3),W(1,7),GC_11,MDL_MC,ZERO,W(1,11))
C     Amplitude(s) for diagram number 33
      CALL FFV6_0(W(1,11),W(1,2),W(1,10),GC_11,AMP(33))
C     Amplitude(s) for diagram number 34
      CALL FFV6_0(W(1,9),W(1,2),W(1,7),GC_11,AMP(34))
      CALL FFV6P0_3(W(1,4),W(1,2),GC_5,ZERO,ZERO,W(1,7))
      CALL FFV6_2(W(1,3),W(1,7),GC_5,MDL_MC,ZERO,W(1,11))
C     Amplitude(s) for diagram number 35
      CALL FFV6_0(W(1,11),W(1,1),W(1,10),GC_11,AMP(35))
C     Amplitude(s) for diagram number 36
      CALL FFV6_0(W(1,9),W(1,1),W(1,7),GC_5,AMP(36))
      CALL FFV6P0_3(W(1,4),W(1,2),GC_2,ZERO,ZERO,W(1,7))
      CALL FFV6_2(W(1,3),W(1,7),GC_2,MDL_MC,ZERO,W(1,11))
C     Amplitude(s) for diagram number 37
      CALL FFV6_0(W(1,11),W(1,1),W(1,10),GC_11,AMP(37))
C     Amplitude(s) for diagram number 38
      CALL FFV6_0(W(1,9),W(1,1),W(1,7),GC_2,AMP(38))
      CALL FFV10_7_3(W(1,4),W(1,2),GC_31,GC_30,MDL_MZ,MDL_WZ,W(1,7))
      CALL FFV10_7_2(W(1,3),W(1,7),GC_31,GC_30,MDL_MC,ZERO,W(1,11))
C     Amplitude(s) for diagram number 39
      CALL FFV6_0(W(1,11),W(1,1),W(1,10),GC_11,AMP(39))
C     Amplitude(s) for diagram number 40
      CALL FFV10_7_0(W(1,9),W(1,1),W(1,7),GC_31,GC_30,AMP(40))
      CALL FFS2_3(W(1,4),W(1,2),GC_42,MDL_MH,MDL_WH,W(1,7))
      CALL FFS2_2(W(1,3),W(1,7),GC_42,MDL_MC,ZERO,W(1,4))
C     Amplitude(s) for diagram number 41
      CALL FFV6_0(W(1,4),W(1,1),W(1,10),GC_11,AMP(41))
C     Amplitude(s) for diagram number 42
      CALL FFS2_0(W(1,9),W(1,1),W(1,7),GC_42,AMP(42))
      CALL FFV6_2(W(1,3),W(1,8),GC_11,MDL_MC,ZERO,W(1,7))
C     Amplitude(s) for diagram number 43
      CALL FFV6_0(W(1,7),W(1,1),W(1,10),GC_11,AMP(43))
C     Amplitude(s) for diagram number 44
      CALL FFV6_0(W(1,9),W(1,1),W(1,8),GC_11,AMP(44))
C     JAMPs contributing to orders ALL_ORDERS=1
      JAMP(1,1)=+AMP(1)+AMP(2)-1D0/6D0*AMP(3)-1D0/6D0*AMP(4)+AMP(5)
     $ +AMP(6)+AMP(7)+AMP(8)+AMP(9)+AMP(10)+AMP(11)+AMP(12)-1D0/2D0
     $ *AMP(15)-1D0/2D0*AMP(16)-1D0/2D0*AMP(25)-1D0/2D0*AMP(26)
     $ -1D0/6D0*AMP(35)-1D0/6D0*AMP(36)+AMP(37)+AMP(38)+AMP(39)
     $ +AMP(40)+AMP(41)+AMP(42)+AMP(43)+AMP(44)
      JAMP(2,1)=+1D0/2D0*AMP(3)+1D0/2D0*AMP(4)-AMP(13)-AMP(14)
     $ +1D0/6D0*AMP(15)+1D0/6D0*AMP(16)-AMP(17)-AMP(18)-AMP(19)
     $ -AMP(20)-AMP(21)-AMP(22)-AMP(23)-AMP(24)+1D0/6D0*AMP(25)
     $ +1D0/6D0*AMP(26)-AMP(27)-AMP(28)-AMP(29)-AMP(30)-AMP(31)
     $ -AMP(32)-AMP(33)-AMP(34)+1D0/2D0*AMP(35)+1D0/2D0*AMP(36)

      MATRIX3 = 0.D0
      DO M = 1, NAMPSO
        DO I = 1, NCOLOR
          ZTEMP = (0.D0,0.D0)
          DO J = 1, NCOLOR
            ZTEMP = ZTEMP + CF(J,I)*JAMP(J,M)
          ENDDO
          DO N = 1, NAMPSO
            IF (CHOSEN_SO_CONFIGS(SQSOINDEX3(M,N))) THEN
              MATRIX3 = MATRIX3 + ZTEMP*DCONJG(JAMP(I,N))/DENOM(I)
            ENDIF
          ENDDO
        ENDDO
      ENDDO

      AMP2(1)=AMP2(1)+AMP(1)*DCONJG(AMP(1))
      AMP2(2)=AMP2(2)+AMP(2)*DCONJG(AMP(2))
      AMP2(4)=AMP2(4)+AMP(4)*DCONJG(AMP(4))
      AMP2(3)=AMP2(3)+AMP(3)*DCONJG(AMP(3))
      AMP2(6)=AMP2(6)+AMP(6)*DCONJG(AMP(6))
      AMP2(5)=AMP2(5)+AMP(5)*DCONJG(AMP(5))
      AMP2(8)=AMP2(8)+AMP(8)*DCONJG(AMP(8))
      AMP2(7)=AMP2(7)+AMP(7)*DCONJG(AMP(7))
      AMP2(10)=AMP2(10)+AMP(10)*DCONJG(AMP(10))
      AMP2(9)=AMP2(9)+AMP(9)*DCONJG(AMP(9))
      AMP2(12)=AMP2(12)+AMP(12)*DCONJG(AMP(12))
      AMP2(11)=AMP2(11)+AMP(11)*DCONJG(AMP(11))
      AMP2(14)=AMP2(14)+AMP(14)*DCONJG(AMP(14))
      AMP2(13)=AMP2(13)+AMP(13)*DCONJG(AMP(13))
      AMP2(26)=AMP2(26)+AMP(26)*DCONJG(AMP(26))
      AMP2(25)=AMP2(25)+AMP(25)*DCONJG(AMP(25))
      AMP2(28)=AMP2(28)+AMP(28)*DCONJG(AMP(28))
      AMP2(27)=AMP2(27)+AMP(27)*DCONJG(AMP(27))
      AMP2(30)=AMP2(30)+AMP(30)*DCONJG(AMP(30))
      AMP2(29)=AMP2(29)+AMP(29)*DCONJG(AMP(29))
      AMP2(32)=AMP2(32)+AMP(32)*DCONJG(AMP(32))
      AMP2(31)=AMP2(31)+AMP(31)*DCONJG(AMP(31))
      AMP2(34)=AMP2(34)+AMP(34)*DCONJG(AMP(34))
      AMP2(33)=AMP2(33)+AMP(33)*DCONJG(AMP(33))
      AMP2(16)=AMP2(16)+AMP(16)*DCONJG(AMP(16))
      AMP2(15)=AMP2(15)+AMP(15)*DCONJG(AMP(15))
      AMP2(18)=AMP2(18)+AMP(18)*DCONJG(AMP(18))
      AMP2(17)=AMP2(17)+AMP(17)*DCONJG(AMP(17))
      AMP2(20)=AMP2(20)+AMP(20)*DCONJG(AMP(20))
      AMP2(19)=AMP2(19)+AMP(19)*DCONJG(AMP(19))
      AMP2(22)=AMP2(22)+AMP(22)*DCONJG(AMP(22))
      AMP2(21)=AMP2(21)+AMP(21)*DCONJG(AMP(21))
      AMP2(24)=AMP2(24)+AMP(24)*DCONJG(AMP(24))
      AMP2(23)=AMP2(23)+AMP(23)*DCONJG(AMP(23))
      AMP2(36)=AMP2(36)+AMP(36)*DCONJG(AMP(36))
      AMP2(35)=AMP2(35)+AMP(35)*DCONJG(AMP(35))
      AMP2(38)=AMP2(38)+AMP(38)*DCONJG(AMP(38))
      AMP2(37)=AMP2(37)+AMP(37)*DCONJG(AMP(37))
      AMP2(40)=AMP2(40)+AMP(40)*DCONJG(AMP(40))
      AMP2(39)=AMP2(39)+AMP(39)*DCONJG(AMP(39))
      AMP2(42)=AMP2(42)+AMP(42)*DCONJG(AMP(42))
      AMP2(41)=AMP2(41)+AMP(41)*DCONJG(AMP(41))
      AMP2(44)=AMP2(44)+AMP(44)*DCONJG(AMP(44))
      AMP2(43)=AMP2(43)+AMP(43)*DCONJG(AMP(43))
      DO I = 1, NCOLOR
        DO M = 1, NAMPSO
          DO N = 1, NAMPSO
            IF (CHOSEN_SO_CONFIGS(SQSOINDEX3(M,N))) THEN
              JAMP2(I)=JAMP2(I)+DABS(DBLE(JAMP(I,M)*DCONJG(JAMP(I,N))))
            ENDIF
          ENDDO
        ENDDO
      ENDDO

      END

C     Set of functions to handle the array indices of the split orders


      INTEGER FUNCTION SQSOINDEX3(ORDERINDEXA, ORDERINDEXB)
C     
C     This functions plays the role of the interference matrix. It can
C      be hardcoded or 
C     made more elegant using hashtables if its execution speed ever
C      becomes a relevant
C     factor. From two split order indices, it return the corresponding
C      index in the squared 
C     order canonical ordering.
C     
C     CONSTANTS
C     

      INTEGER    NSO, NSQUAREDSO, NAMPSO
      PARAMETER (NSO=1, NSQUAREDSO=1, NAMPSO=1)
C     
C     ARGUMENTS
C     
      INTEGER ORDERINDEXA, ORDERINDEXB
C     
C     LOCAL VARIABLES
C     
      INTEGER I, SQORDERS(NSO)
      INTEGER AMPSPLITORDERS(NAMPSO,NSO)
      DATA (AMPSPLITORDERS(  1,I),I=  1,  1) /    1/
C     
C     FUNCTION
C     
      INTEGER SOINDEX_FOR_SQUARED_ORDERS3
C     
C     BEGIN CODE
C     
      DO I=1,NSO
        SQORDERS(I)=AMPSPLITORDERS(ORDERINDEXA,I)+AMPSPLITORDERS(ORDERI
     $   NDEXB,I)
      ENDDO
      SQSOINDEX3=SOINDEX_FOR_SQUARED_ORDERS3(SQORDERS)
      END

      INTEGER FUNCTION SOINDEX_FOR_SQUARED_ORDERS3(ORDERS)
C     
C     This functions returns the integer index identifying the squared
C      split orders list passed in argument which corresponds to the
C      values of the following list of couplings (and in this order).
C     []
C     
C     CONSTANTS
C     
      INTEGER    NSO, NSQSO, NAMPSO
      PARAMETER (NSO=1, NSQSO=1, NAMPSO=1)
C     
C     ARGUMENTS
C     
      INTEGER ORDERS(NSO)
C     
C     LOCAL VARIABLES
C     
      INTEGER I,J
      INTEGER SQSPLITORDERS(NSQSO,NSO)
      DATA (SQSPLITORDERS(  1,I),I=  1,  1) /    2/
C     
C     BEGIN CODE
C     
      DO I=1,NSQSO
        DO J=1,NSO
          IF (ORDERS(J).NE.SQSPLITORDERS(I,J)) GOTO 1009
        ENDDO
        SOINDEX_FOR_SQUARED_ORDERS3 = I
        RETURN
 1009   CONTINUE
      ENDDO

      WRITE(*,*) 'ERROR:: Stopping function SOINDEX_FOR_SQUARED_ORDERS'
      WRITE(*,*) 'Could not find squared orders ',(ORDERS(I),I=1,NSO)
      STOP

      END

      SUBROUTINE GET_NSQSO_BORN3(NSQSO)
C     
C     Simple subroutine returning the number of squared split order
C     contributions returned when calling smatrix_split_orders 
C     

      INTEGER    NSQUAREDSO
      PARAMETER  (NSQUAREDSO=1)

      INTEGER NSQSO

      NSQSO=NSQUAREDSO

      END

