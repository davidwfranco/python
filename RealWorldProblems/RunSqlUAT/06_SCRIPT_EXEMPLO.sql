----------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------
---- AUTOR - PAULO LEON ----------------------------------------------------------------------
---- DATA  - 01-11-2017 ----------------------------------------------------------------------
---- TITULO- 10-LAADMD-380.sql ---------------------------------------------------------------
---- DESCRICAO: VVVVVVVVV qqqqqqqqqqqq ------------------------------------------------------------
---- JIRA: LAASIC-866 LAADMD-380 -------------------------------------------------------------
----------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------

----------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------
---- PRE EXECUTION ---------------------------------------------------------------------------
----------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------

SET LINESIZE 10000;
SET TIMING ON;
SET ECHO ON;
SET SERVEROUTPUT ON SIZE UNLIMITED;
WHENEVER SQLERROR EXIT FAILURE;
SPOOL c:/temp/06-SCRIPT_EXEMPLO.log;
ALTER SESSION SET CURRENT_SCHEMA=BATCHMODULE;

INSERT INTO ABC_CDE (NAME, XPTO, DESCRIPTION, ABS, USER_NAME, OS_USER, OS_HOST)
VALUES(
  'AAAAAAAAAAAAAA',
  '1117.11',
  'Sbrublhouws',  
  'ASDASDASDASD',
  (SELECT SYS_CONTEXT ('USERENV', 'SESSION_USER') FROM DUAL),
  (SELECT SYS_CONTEXT ('USERENV', 'OS_USER') FROM DUAL),
  (SELECT SYS_CONTEXT ('USERENV', 'HOST') FROM DUAL)
);

COMMIT;

----------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------
---- EXECUTION -------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------

CREATE TABLE AAAAAAAAAAAAAAAAA(
	ID										NUMBER(22) NOT NULL,
	OPERATION_qqqqqqqqqqqq_ID		NUMBER(22) NOT NULL,
  ROLE_TYPE							VARCHAR2(4000),
	AMOUNT			VARCHAR2(4000),
	CONSTRAINT COMMqqqqqqqqqqqq_PK PRIMARY KEY (ID),
	CONSTRAINT COMMqqqqqqqqqqqq_OPERqqqqqqqqqqqq_FK
		FOREIGN KEY (OPERATION_qqqqqqqqqqqq_ID)
		REFERENCES OPERATION_qqqqqqqqqqqq(OPERATION_qqqqqqqqqqqq_ID) ENABLE);

CREATE SEQUENCE SQ_AAAAAAAAAAAAAAAAA
 MINVALUE 1
 START WITH 1
 INCREMENT BY 1
 CACHE 20;

CREATE TABLE AAAAAAAAAAAAAAAAA_AUDIT(
	ID										NUMBER(22) NOT NULL,
	OPERATION_qqqqqqqqqqqq_ID		NUMBER(22) NOT NULL,
  ROLE_TYPE							VARCHAR2(4000),
	AMOUNT								VARCHAR2(4000),
	REV										NUMBER(22),
	REVTYPE								NUMBER(22),
	CONSTRAINT COMCONFAUD_PK PRIMARY KEY (ID)
);

CREATE TABLE VVVVVVVVV(
	ID							NUMBER(22) NOT NULL,
	AMOUNT 					NUMBER(38,8),
	ROLE_ID					NUMBER(22),
	EVENT_TYPE_ID		NUMBER(22),
	OPERATION_ID		NUMBER(22),
	CONSTRAINT VVVVVVVVV_PK PRIMARY KEY (ID),
	CONSTRAINT VVVVVVVVV_OPERATION_FK
		FOREIGN KEY (OPERATION_ID)
		REFERENCES OPERATION(ID) ENABLE);

CREATE SEQUENCE SQ_VVVVVVVVV
 MINVALUE 1
 START WITH 1
 INCREMENT BY 1
 CACHE 20;

COMMENT ON COLUMN AAAAAAAAAAAAAAAAA.ID IS 'Primary key - ID (PK) of VVVVVVVVV qqqqqqqqqqqquration - Uses SQ_AAAAAAAAAAAAAAAAA';
COMMENT ON COLUMN AAAAAAAAAAAAAAAAA.OPERATION_qqqqqqqqqqqq_ID IS 'FK - ID (PK) of Operation qqqqqqqqqqqquration';
COMMENT ON COLUMN AAAAAAAAAAAAAAAAA.ROLE_TYPE IS 'Role type';
COMMENT ON COLUMN AAAAAAAAAAAAAAAAA.AMOUNT IS 'Ammount of the VVVVVVVVV';
COMMENT ON COLUMN AAAAAAAAAAAAAAAAA_AUDIT.ID IS 'Primary key - ID (PK) of VVVVVVVVV qqqqqqqqqqqquration';
COMMENT ON COLUMN AAAAAAAAAAAAAAAAA_AUDIT.OPERATION_qqqqqqqqqqqq_ID IS 'ID (PK) of Operation qqqqqqqqqqqquration';
COMMENT ON COLUMN AAAAAAAAAAAAAAAAA_AUDIT.ROLE_TYPE IS 'Role type';
COMMENT ON COLUMN AAAAAAAAAAAAAAAAA_AUDIT.AMOUNT IS 'Ammount of the VVVVVVVVV';
COMMENT ON COLUMN AAAAAAAAAAAAAAAAA_AUDIT.REV IS 'Revision';
COMMENT ON COLUMN AAAAAAAAAAAAAAAAA_AUDIT.REVTYPE IS 'Revision type';
COMMENT ON COLUMN VVVVVVVVV.ID IS 'Primary key - ID (PK) of VVVVVVVVV - Uses SQ_VVVVVVVVV';
COMMENT ON COLUMN VVVVVVVVV.AMOUNT IS 'Ammount of the VVVVVVVVV';
COMMENT ON COLUMN VVVVVVVVV.ROLE_ID IS 'ID of Role';
COMMENT ON COLUMN VVVVVVVVV.EVENT_TYPE_ID IS 'ID (PK) of event type';
COMMENT ON COLUMN VVVVVVVVV.OPERATION_ID IS 'FK - ID (PK) of Operation';

----------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------
---- FINISH EXECUTION ------------------------------------------------------------------------
----------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------

COMMIT;

spool off;
