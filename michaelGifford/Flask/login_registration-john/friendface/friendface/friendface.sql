-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema friendface
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema friendface
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `friendface` DEFAULT CHARACTER SET utf8 ;
USE `friendface` ;

-- -----------------------------------------------------
-- Table `friendface`.`blogs`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `friendface`.`blogs` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL,
  `created_at` DATETIME NULL,
  `modified_at` DATETIME NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `friendface`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `friendface`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NULL,
  `last_name` VARCHAR(45) NULL,
  `email` VARCHAR(155) NULL,
  `created_at` DATETIME NULL,
  `modifed_at` DATETIME NULL,
  `password` VARCHAR(255) NULL,
  `profile` VARCHAR(255) NULL,
  `alias` VARCHAR(45) NULL,
  `birthday` DATETIME NULL,
  `bio` MEDIUMTEXT NULL,
  `avatar` VARCHAR(255) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `friendface`.`admins`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `friendface`.`admins` (
  `id` INT NOT NULL,
  `blog_id` INT NOT NULL,
  `user_id` INT NOT NULL,
  `created_at` DATETIME NULL,
  `modified_at` DATETIME NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_admins_blogs_idx` (`blog_id` ASC),
  INDEX `fk_admins_users1_idx` (`user_id` ASC),
  CONSTRAINT `fk_admins_blogs`
    FOREIGN KEY (`blog_id`)
    REFERENCES `friendface`.`blogs` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_admins_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `friendface`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `friendface`.`posts`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `friendface`.`posts` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(155) NULL,
  `content` LONGTEXT NULL,
  `blog_id` INT NOT NULL,
  `user_id` INT NOT NULL,
  `created_at` DATETIME NULL,
  `modified_at` DATETIME NULL,
  `subhead` VARCHAR(255) NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_posts_blogs1_idx` (`blog_id` ASC),
  INDEX `fk_posts_users1_idx` (`user_id` ASC),
  CONSTRAINT `fk_posts_blogs1`
    FOREIGN KEY (`blog_id`)
    REFERENCES `friendface`.`blogs` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_posts_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `friendface`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `friendface`.`logs`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `friendface`.`logs` (
  `id` INT NOT NULL,
  `ip` VARCHAR(255) NULL,
  `created_at` DATETIME NULL,
  `modified_at` DATETIME NULL,
  `post_id` INT NOT NULL,
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_logs_posts1_idx` (`post_id` ASC),
  INDEX `fk_logs_users1_idx` (`user_id` ASC),
  CONSTRAINT `fk_logs_posts1`
    FOREIGN KEY (`post_id`)
    REFERENCES `friendface`.`posts` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_logs_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `friendface`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `friendface`.`comments`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `friendface`.`comments` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `comment` VARCHAR(255) NULL,
  `created_at` DATETIME NULL,
  `modified_at` DATETIME NULL,
  `post_id` INT NOT NULL,
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_comments_posts1_idx` (`post_id` ASC),
  INDEX `fk_comments_users1_idx` (`user_id` ASC),
  CONSTRAINT `fk_comments_posts1`
    FOREIGN KEY (`post_id`)
    REFERENCES `friendface`.`posts` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_comments_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `friendface`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `friendface`.`files`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `friendface`.`files` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NULL,
  `post_id` INT NOT NULL,
  `created_at` DATETIME NULL,
  `modified_at` DATETIME NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_files_posts1_idx` (`post_id` ASC),
  CONSTRAINT `fk_files_posts1`
    FOREIGN KEY (`post_id`)
    REFERENCES `friendface`.`posts` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
