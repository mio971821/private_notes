create table �Һ�
(
	�ҵ{�N�X	char(6), --- char:�T�w���צr�� RS156E
    �Ǩt�֤߽ҵ{��O���� varchar2(256), --- varchar2:�i�ܪ��צr��
	�q�l�l��H�c varchar2(80),
    �ǳN���	varchar2(4), --- 100%
	�ҵ{���n�ζi�� varchar2(256),
    �Үֶ��ؤε��q�з�_��� varchar2(256),
	�ҵ{�оǥؼ� varchar2(256),
    �ǫe��ةί�O�ݨD varchar2(80),
	�W�d varchar2(256),
    ���G�ɦV���ҵ{�]�p varchar2(256),
	�ҷ~�Яq�ɶ� varchar2(80),
    �½һy�� varchar2(10),
	�½ҩʽ� varchar2(10),
    �H�ƤW��	number(3),
	��_�b�Ǧ~ char(3),
    �}�Үɼ� number(2),
    
	primary key	(�ҵ{�N�X)
)
/
create table �ҵ{���
(
	�ҵ{�N�X	char(6),
	�ҵ{�W��	varchar2(30),
	�}�үZ��	varchar2(12),
	��_���	    char(6),        --- ����/���
    �½ұЮv	varchar2(32),
	�W�ұЫ�	varchar2(32),
    �ǵ{���O	varchar2(10),
	�ҵ{���O	varchar2(32),
    �W�Үɶ�	varchar2(32),
	���Z�оǽҵ{ varchar2(3),  --- �P�B/�D�P�B
	�Ǥ��� number(2),
	�Ƶ� varchar2(256),
    
	primary key	(�ҵ{�N�X)
)
/
create table ��Ҹ��
(
    �ҵ{�N�X char(6),
    �}�ҤH�� number(3),
    �w��H�� number(5),
    ��ҦW�B number(5),
    �z��l�B number(3),
    �{���q�n�O�H�� number(5),
    �h�~�n�O�H�� number(5),
    primary key (�ҵ{�N�X)
)
/
create table �ǥͿ�ҲM��
( 
    �Ǹ� number(8),
    �ҵ{�N�X char(6),
    �M�����O varchar2(256),    --- �׽�/            �l��/�n�O/����45
    �׽ұ��p varchar2(256),    --- �h��/���b��/����
    primary key (�Ǹ�, �ҵ{�N�X)
)
/
create table �ǥ�
(
    �t�� varchar2(32),
    �Ǹ� number(8), 
    �m�W varchar2(10),
    �ʧO char(3),
    primary key (�Ǹ�)
)

create table �U�t���׾Ǥ�
(
    �Ǹ� number(8),
    ���� number(2), 
    ��� number(2),
    �q�Ѱ�¦���� number(2),
    �q�ѩ������ number(2),
    �ۥѿ�� number(2),
    �򥻪��� number(2),
    ���^�y�ҵ{ number(2),
    �^���OŲ�w varchar2(12),  ---���Ū��
    primary key (�Ǹ�)
)
/
ALTER TABLE �Һ�
 ADD CONSTRAINT �Һ�_�ҵ{���_FK
 FOREIGN KEY (�ҵ{�N�X)
 REFERENCES �ҵ{��� (�ҵ{�N�X) ENABLE;
 
ALTER TABLE ��Ҹ��
 ADD CONSTRAINT ��Ҹ��_�ҵ{���_FK
 FOREIGN KEY (�ҵ{�N�X)
 REFERENCES �ҵ{��� (�ҵ{�N�X) ENABLE;
 
ALTER TABLE �ǥͿ�ҲM��
 ADD CONSTRAINT �ǥͿ�ҲM��_�ҵ{���_FK
 FOREIGN KEY (�ҵ{�N�X)
 REFERENCES �ҵ{��� (�ҵ{�N�X) ENABLE;
 
ALTER TABLE �ǥͿ�ҲM��
 ADD CONSTRAINT �ǥͿ�ҲM��_�ǥ�_FK
 FOREIGN KEY (�Ǹ�)
 REFERENCES �ǥ� (�Ǹ�) ENABLE;
 
ALTER TABLE �U�t���׾Ǥ�
 ADD CONSTRAINT �U�t���׾Ǥ�_�ǥ�_FK
 FOREIGN KEY (�Ǹ�)
 REFERENCES �ǥ� (�Ǹ�) ENABLE;
 
---ALTER TABLE �Һ� DROP CONSTRAINT �Һ�_�ҵ{���_FK;
---ALTER TABLE ��Ҹ�� DROP CONSTRAINT ��Ҹ��_�ҵ{���_FK;
---ALTER TABLE �ǥͿ�ҲM�� DROP CONSTRAINT �ǥͿ�ҲM��_�ҵ{���_FK;
---ALTER TABLE �ǥͿ�ҲM�� DROP CONSTRAINT �ǥͿ�ҲM��_�ǥ�_FK;
---ALTER TABLE �U�t���׾Ǥ� DROP CONSTRAINT �U�t���׾Ǥ�_�ǥ�_FK;