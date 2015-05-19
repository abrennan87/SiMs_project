      SUBROUTINE SMATRIX1(P,ANS)
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
C     Process: s s~ > g g chi chi~ WEIGHTED=4
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
      PARAMETER (NGRAPHS=8)
      INTEGER    NDIAGS
      PARAMETER (NDIAGS=8)
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
      REAL*8 T,MATRIX1
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
            T=MATRIX1(P ,NHEL(1,I),JC(1))
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
          T=MATRIX1(P ,NHEL(1,I),JC(1))
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
          ANS=ANS*AMP2(SUBDIAG(1))/XTOT
        ELSE
          ANS=0D0
        ENDIF
      ENDIF
      ANS=ANS/DBLE(IDEN)
      END


      REAL*8 FUNCTION MATRIX1(P,NHEL,IC)
C     
C     Generated by MadGraph5_aMC@NLO v. 2.2.2, 2014-11-06
C     By the MadGraph5_aMC@NLO Development Team
C     Visit launchpad.net/madgraph5 and amcatnlo.web.cern.ch
C     
C     Returns amplitude squared summed/avg over colors
C     for the point with external lines W(0:6,NEXTERNAL)
C     
C     Process: s s~ > g g chi chi~ WEIGHTED=4
C     
      IMPLICIT NONE
C     
C     CONSTANTS
C     
      INTEGER    NGRAPHS
      PARAMETER (NGRAPHS=8)
      INCLUDE 'genps.inc'
      INCLUDE 'nexternal.inc'
      INCLUDE 'maxamps.inc'
      INTEGER    NWAVEFUNCS,     NCOLOR
      PARAMETER (NWAVEFUNCS=9, NCOLOR=2)
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
      INTEGER SQSOINDEX1
C     
C     GLOBAL VARIABLES
C     
      DOUBLE PRECISION AMP2(MAXAMPS), JAMP2(0:MAXFLOW)
      COMMON/TO_AMPS/  AMP2,       JAMP2
      INCLUDE 'coupl.inc'
C     
C     COLOR DATA
C     
      DATA DENOM(1)/3/
      DATA (CF(I,  1),I=  1,  2) /   16,   -2/
C     1 T(3,4,2,1)
      DATA DENOM(2)/3/
      DATA (CF(I,  2),I=  1,  2) /   -2,   16/
C     1 T(4,3,2,1)
C     ----------
C     BEGIN CODE
C     ----------
      CALL IXXXXX(P(0,1),MDL_MS,NHEL(1),+1*IC(1),W(1,1))
      CALL OXXXXX(P(0,2),MDL_MS,NHEL(2),-1*IC(2),W(1,2))
      CALL VXXXXX(P(0,3),ZERO,NHEL(3),+1*IC(3),W(1,3))
      CALL VXXXXX(P(0,4),ZERO,NHEL(4),+1*IC(4),W(1,4))
      CALL OXXXXX(P(0,5),MDL_MCHI,NHEL(5),+1*IC(5),W(1,5))
      CALL IXXXXX(P(0,6),MDL_MCHI,NHEL(6),-1*IC(6),W(1,6))
      CALL VVV2P0_1(W(1,3),W(1,4),GC_4,ZERO,ZERO,W(1,7))
      CALL FFV6_3(W(1,6),W(1,5),GC_12,MDL_MXI,MDL_WXI,W(1,8))
      CALL FFV6_1(W(1,2),W(1,7),GC_5,MDL_MS,ZERO,W(1,6))
C     Amplitude(s) for diagram number 1
      CALL FFV6_0(W(1,1),W(1,6),W(1,8),GC_14,AMP(1))
      CALL FFV6_2(W(1,1),W(1,7),GC_5,MDL_MS,ZERO,W(1,6))
C     Amplitude(s) for diagram number 2
      CALL FFV6_0(W(1,6),W(1,2),W(1,8),GC_14,AMP(2))
      CALL FFV6_1(W(1,2),W(1,3),GC_5,MDL_MS,ZERO,W(1,6))
      CALL FFV6_2(W(1,1),W(1,4),GC_5,MDL_MS,ZERO,W(1,7))
C     Amplitude(s) for diagram number 3
      CALL FFV6_0(W(1,7),W(1,6),W(1,8),GC_14,AMP(3))
      CALL FFV6_1(W(1,6),W(1,4),GC_5,MDL_MS,ZERO,W(1,5))
C     Amplitude(s) for diagram number 4
      CALL FFV6_0(W(1,1),W(1,5),W(1,8),GC_14,AMP(4))
      CALL FFV6_2(W(1,1),W(1,3),GC_5,MDL_MS,ZERO,W(1,5))
      CALL FFV6_1(W(1,2),W(1,4),GC_5,MDL_MS,ZERO,W(1,6))
C     Amplitude(s) for diagram number 5
      CALL FFV6_0(W(1,5),W(1,6),W(1,8),GC_14,AMP(5))
      CALL FFV6_2(W(1,5),W(1,4),GC_5,MDL_MS,ZERO,W(1,9))
C     Amplitude(s) for diagram number 6
      CALL FFV6_0(W(1,9),W(1,2),W(1,8),GC_14,AMP(6))
      CALL FFV6_1(W(1,6),W(1,3),GC_5,MDL_MS,ZERO,W(1,9))
C     Amplitude(s) for diagram number 7
      CALL FFV6_0(W(1,1),W(1,9),W(1,8),GC_14,AMP(7))
      CALL FFV6_2(W(1,7),W(1,3),GC_5,MDL_MS,ZERO,W(1,9))
C     Amplitude(s) for diagram number 8
      CALL FFV6_0(W(1,9),W(1,2),W(1,8),GC_14,AMP(8))
C     JAMPs contributing to orders ALL_ORDERS=1
      JAMP(1,1)=+IMAG1*AMP(1)+IMAG1*AMP(2)-AMP(3)-AMP(4)-AMP(8)
      JAMP(2,1)=-IMAG1*AMP(1)-IMAG1*AMP(2)-AMP(5)-AMP(6)-AMP(7)

      MATRIX1 = 0.D0
      DO M = 1, NAMPSO
        DO I = 1, NCOLOR
          ZTEMP = (0.D0,0.D0)
          DO J = 1, NCOLOR
            ZTEMP = ZTEMP + CF(J,I)*JAMP(J,M)
          ENDDO
          DO N = 1, NAMPSO
            IF (CHOSEN_SO_CONFIGS(SQSOINDEX1(M,N))) THEN
              MATRIX1 = MATRIX1 + ZTEMP*DCONJG(JAMP(I,N))/DENOM(I)
            ENDIF
          ENDDO
        ENDDO
      ENDDO

      AMP2(1)=AMP2(1)+AMP(1)*DCONJG(AMP(1))
      AMP2(2)=AMP2(2)+AMP(2)*DCONJG(AMP(2))
      AMP2(3)=AMP2(3)+AMP(3)*DCONJG(AMP(3))
      AMP2(4)=AMP2(4)+AMP(4)*DCONJG(AMP(4))
      AMP2(5)=AMP2(5)+AMP(5)*DCONJG(AMP(5))
      AMP2(6)=AMP2(6)+AMP(6)*DCONJG(AMP(6))
      AMP2(7)=AMP2(7)+AMP(7)*DCONJG(AMP(7))
      AMP2(8)=AMP2(8)+AMP(8)*DCONJG(AMP(8))
      DO I = 1, NCOLOR
        DO M = 1, NAMPSO
          DO N = 1, NAMPSO
            IF (CHOSEN_SO_CONFIGS(SQSOINDEX1(M,N))) THEN
              JAMP2(I)=JAMP2(I)+DABS(DBLE(JAMP(I,M)*DCONJG(JAMP(I,N))))
            ENDIF
          ENDDO
        ENDDO
      ENDDO

      END

C     Set of functions to handle the array indices of the split orders


      INTEGER FUNCTION SQSOINDEX1(ORDERINDEXA, ORDERINDEXB)
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
      INTEGER SOINDEX_FOR_SQUARED_ORDERS1
C     
C     BEGIN CODE
C     
      DO I=1,NSO
        SQORDERS(I)=AMPSPLITORDERS(ORDERINDEXA,I)+AMPSPLITORDERS(ORDERI
     $   NDEXB,I)
      ENDDO
      SQSOINDEX1=SOINDEX_FOR_SQUARED_ORDERS1(SQORDERS)
      END

      INTEGER FUNCTION SOINDEX_FOR_SQUARED_ORDERS1(ORDERS)
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
        SOINDEX_FOR_SQUARED_ORDERS1 = I
        RETURN
 1009   CONTINUE
      ENDDO

      WRITE(*,*) 'ERROR:: Stopping function SOINDEX_FOR_SQUARED_ORDERS'
      WRITE(*,*) 'Could not find squared orders ',(ORDERS(I),I=1,NSO)
      STOP

      END

      SUBROUTINE GET_NSQSO_BORN1(NSQSO)
C     
C     Simple subroutine returning the number of squared split order
C     contributions returned when calling smatrix_split_orders 
C     

      INTEGER    NSQUAREDSO
      PARAMETER  (NSQUAREDSO=1)

      INTEGER NSQSO

      NSQSO=NSQUAREDSO

      END

