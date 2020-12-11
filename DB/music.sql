BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "music" (
	"Id"	INTEGER,
	"file_id"	TEXT,
	"right_answer"	TEXT,
	"right_artist"	TEXT,
	"wrong_answer"	TEXT
);
INSERT INTO "music" VALUES (1,'AwACAgIAAxkDAAIBOl_QtNdctUyjkQWnurOPylRvVSgqAAJADAACXc6JSgTE9nUNQeM6HgQ','PointsOfAuthority','LinkinPark','EyeofaTiger,sobeautiful,loveyou');
INSERT INTO "music" VALUES (2,'AwACAgIAAxkDAAIBMF_QtIkGEV5hmDnMRa4ZImDmuWqEAAI6DAACXc6JSh9bJsSFRjdtHgQ','PointsOfAuthority','LinkinPark','Windofchange,haligali,onewayticket');
INSERT INTO "music" VALUES (3,'AwACAgIAAxkDAAIBNF_QtKNvoRH9MeXsSM-a-sYbJhLcAAI8DAACXc6JSu2rqjVE2pnRHgQ','EyeofaTiger','Survivor','Windofchange,haligali,onewayticket');
INSERT INTO "music" VALUES (4,'AwACAgIAAxkDAAIBNl_QtK8_-y8LB5xc2wnzBEH608CzAAI9DAACXc6JSqo2Vixh8-mgHgQ','EyeofaTiger','Survivor','Windofchange,haligali,onewayticket');
INSERT INTO "music" VALUES (5,'AwACAgIAAxkDAAIBOF_QtLtV5BSekeZ9y7oCvOKFM7wFAAI-DAACXc6JSjp0FVldR9g7HgQ','BetweenAngelsandInsects','PapaRoach','Windofchange,haligali,onewayticket');
INSERT INTO "music" VALUES (6,'AwACAgIAAxkDAAIBMl_QtJad6N6wW5BLhHbY7mZ5sajtAAI7DAACXc6JSsYRsZjH6jhEHgQ','LastResort','PapaRoach','EyeofaTiger,sobeautiful,loveyou');
COMMIT;
