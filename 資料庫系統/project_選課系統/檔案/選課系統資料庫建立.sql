create table 課綱
(
	課程代碼	char(6), --- char:固定長度字串 RS156E
    學系核心課程能力指標 varchar2(256), --- varchar2:可變長度字串
	電子郵件信箱 varchar2(80),
    學術比例	varchar2(4), --- 100%
	課程綱要及進度 varchar2(256),
    考核項目及評量標準_比例 varchar2(256),
	課程教學目標 varchar2(256),
    學前科目或能力需求 varchar2(80),
	規範 varchar2(256),
    成果導向之課程設計 varchar2(256),
	課業請益時間 varchar2(80),
    授課語言 varchar2(10),
	授課性質 varchar2(10),
    人數上限	number(3),
	全_半學年 char(3),
    開課時數 number(2),
    
	primary key	(課程代碼)
)
/
create table 課程資料
(
	課程代碼	char(6),
	課程名稱	varchar2(30),
	開課班級	varchar2(12),
	必_選修	    char(6),        --- 必修/選修
    授課教師	varchar2(32),
	上課教室	varchar2(32),
    學程類別	varchar2(10),
	課程類別	varchar2(32),
    上課時間	varchar2(32),
	遠距教學課程 varchar2(3),  --- 同步/非同步
	學分數 number(2),
	備註 varchar2(256),
    
	primary key	(課程代碼)
)
/
create table 選課資料
(
    課程代碼 char(6),
    開課人數 number(3),
    已選人數 number(5),
    選課名額 number(5),
    篩選餘額 number(3),
    現階段登記人數 number(5),
    去年登記人數 number(5),
    primary key (課程代碼)
)
/
create table 學生選課清單
( 
    學號 number(8),
    課程代碼 char(6),
    清單類別 varchar2(256),    --- 修課/            追蹤/登記/遞補45
    修課情況 varchar2(256),    --- 退選/正在修/完成
    primary key (學號, 課程代碼)
)
/
create table 學生
(
    系級 varchar2(32),
    學號 number(8), 
    姓名 varchar2(10),
    性別 char(3),
    primary key (學號)
)

create table 各系應修學分
(
    學號 number(8),
    必修 number(2), 
    選修 number(2),
    通識基礎必修 number(2),
    通識延伸選修 number(2),
    自由選修 number(2),
    基本知能 number(2),
    全英語課程 number(2),
    英文能力鑑定 varchar2(12),  ---中級初試
    primary key (學號)
)
/
ALTER TABLE 課綱
 ADD CONSTRAINT 課綱_課程資料_FK
 FOREIGN KEY (課程代碼)
 REFERENCES 課程資料 (課程代碼) ENABLE;
 
ALTER TABLE 選課資料
 ADD CONSTRAINT 選課資料_課程資料_FK
 FOREIGN KEY (課程代碼)
 REFERENCES 課程資料 (課程代碼) ENABLE;
 
ALTER TABLE 學生選課清單
 ADD CONSTRAINT 學生選課清單_課程資料_FK
 FOREIGN KEY (課程代碼)
 REFERENCES 課程資料 (課程代碼) ENABLE;
 
ALTER TABLE 學生選課清單
 ADD CONSTRAINT 學生選課清單_學生_FK
 FOREIGN KEY (學號)
 REFERENCES 學生 (學號) ENABLE;
 
ALTER TABLE 各系應修學分
 ADD CONSTRAINT 各系應修學分_學生_FK
 FOREIGN KEY (學號)
 REFERENCES 學生 (學號) ENABLE;
 
---ALTER TABLE 課綱 DROP CONSTRAINT 課綱_課程資料_FK;
---ALTER TABLE 選課資料 DROP CONSTRAINT 選課資料_課程資料_FK;
---ALTER TABLE 學生選課清單 DROP CONSTRAINT 學生選課清單_課程資料_FK;
---ALTER TABLE 學生選課清單 DROP CONSTRAINT 學生選課清單_學生_FK;
---ALTER TABLE 各系應修學分 DROP CONSTRAINT 各系應修學分_學生_FK;