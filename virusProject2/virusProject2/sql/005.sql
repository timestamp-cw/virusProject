--创建mysql定时任务
CREATE EVENT event_my_one ON SCHEDULE EVERY 1 DAY STARTS '2022-04-11 18:00:00' ON COMPLETION PRESERVE ENABLE DO
BEGIN
		CALL insert_now_data ();
CALL insert_now_province_add ();
END;
--查询mysql事件
SELECT * FROM information_schema.events limit 10