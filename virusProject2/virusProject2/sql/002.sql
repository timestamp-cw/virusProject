--table2
--第一次汇总疫情数据
CREATE TABLE
IF
	NOT EXISTS table2 AS SELECT
	`date`,
	`province`,
	`cases`,
	`recovered`,
	`death`
FROM
	ds_table2 UNION
SELECT
	`date`,
	`province`,
	`confirmSum`,
	`cureSum`,
	`deathSum`
FROM
	bd_table3;
--为总表添加唯一约束
ALTER TABLE table2 ADD UNIQUE ( date, province );
--表内省份拼音转省份汉字
UPDATE table2 A,
province_contranst B
SET A.province = B.chinese_character
WHERE
	A.province = B.chinese_pinyin;
--向总疫情数据插入每日疫情数据
INSERT INTO table2 ( `date`, province, cases, recovered, death ) SELECT
`date`,
`province`,
`confirmSum`,
`cureSum`,
`deathSum`
FROM
	bd_table3
WHERE
	date = CURRENT_DATE ();
--table3
--每日新增总表
CREATE TABLE
IF
	NOT EXISTS table3 (
		`date` date,
		`province` VARCHAR ( 255 ),
		`casesAdd` INT,
		`recoveredAdd` INT,
		`deathAdd` INT,
	PRIMARY KEY ( `date`, `province` )
	)
--第一次对table3填充数据
call virusproject.gen_province_add();
--每日对tablw3填充数据
call virusproject.insert_now_province_add();

