/*
 Navicat Premium Data Transfer

 Source Server         : Adminstrastor
 Source Server Type    : MySQL
 Source Server Version : 50725
 Source Host           : localhost:3306
 Source Schema         : financial_data

 Target Server Type    : MySQL
 Target Server Version : 50725
 File Encoding         : 65001

 Date: 14/07/2019 16:13:14
*/

SET NAMES utf8mb4;

CREATE DATABASE IF NOT EXISTS `financial_data` CHARACTER SET 'utf8' COLLATE 'utf8_general_ci';
USE `financial_data`;
-- ----------------------------
-- Table structure for file
-- ----------------------------

DROP TABLE IF EXISTS `file`;
CREATE TABLE IF NOT EXISTS `file` (
   `fileID` INT UNSIGNED NOT NULL AUTO_INCREMENT,
   `fileName` VARCHAR(200) NOT NULL,
   `fileUrl` VARCHAR(200) NOT NULL DEFAULT '0',
   `fileDate` VARCHAR(50) NOT NULL,
   `fileType` VARCHAR(50) NOT NULL,
   PRIMARY KEY (`fileID`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
ALTER TABLE file AUTO_INCREMENT=100; 

INSERT INTO file VALUES(NULL,'2018年省级收支预算表', 'http://www.henan.gov.cn/att/0/10/33/52/10335219_357660.xls', '2018', '省政府预算');
INSERT INTO file VALUES(NULL,'2019年省级预算及说明.pdf', 'https://file.henan.gov.cn/4500000001/2019-02-01/1549012260689wvMD9z0e.pdf', '2019', '省政府预算');
INSERT INTO file VALUES(NULL,'2019年省级预算及说明.pdf', 'https://file.henan.gov.cn/4500000001/2019-02-01/1549012260689wvMD9z0e.pdf', '2019', '省政府预算');

-- ----------------------------
-- Table structure for login
-- ----------------------------
DROP TABLE IF EXISTS `login`;
CREATE TABLE IF NOT EXISTS `login` (
   `loginID` INT UNSIGNED NOT NULL AUTO_INCREMENT,
   `loginUser` VARCHAR(200) NOT NULL,
   `loginPass` VARCHAR(200) NOT NULL,
   `loginLevel` VARCHAR(200) NOT NULL,
   PRIMARY KEY(`loginID`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
ALTER TABLE login AUTO_INCREMENT=100; 

INSERT INTO login VALUES(NULL,'1','1','管理员')