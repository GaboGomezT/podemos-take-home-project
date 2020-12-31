-- MySQL Script generated by MySQL Workbench
-- dom 09 ago 2015 10:54:25 CDT
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema podemos_eval
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema podemos_eval
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `podemos_eval` DEFAULT CHARACTER SET utf8 ;
USE `podemos_eval` ;

-- -----------------------------------------------------
-- Table `podemos_eval`.`Grupos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `podemos_eval`.`Grupos` (
  `id` VARCHAR(5) NOT NULL COMMENT '',
  `nombre` VARCHAR(20) NOT NULL COMMENT '',
  PRIMARY KEY (`id`)  COMMENT '')
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `podemos_eval`.`Cuentas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `podemos_eval`.`Cuentas` (
  `id` VARCHAR(5) NOT NULL COMMENT '',
  `grupo_id` VARCHAR(5) NOT NULL COMMENT '',
  `estatus` VARCHAR(15) NOT NULL COMMENT '',
  `monto` DECIMAL(15,2) NOT NULL COMMENT '',
  `saldo` DECIMAL(15,2) NOT NULL COMMENT '',
  PRIMARY KEY (`id`)  COMMENT '',
  INDEX `fk_grupo_idx` (`grupo_id` ASC)  COMMENT '',
  CONSTRAINT `fk_Cuentas_1`
    FOREIGN KEY (`grupo_id`)
    REFERENCES `podemos_eval`.`Grupos` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `podemos_eval`.`CalendarioPagos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `podemos_eval`.`CalendarioPagos` (
  `id` INT(11) NOT NULL COMMENT '',
  `cuenta_id` VARCHAR(5) NOT NULL COMMENT '',
  `num_pago` INT(11) NOT NULL COMMENT '',
  `monto` DECIMAL(15,2) NOT NULL COMMENT '',
  `fecha_pago` DATE NOT NULL COMMENT '',
  `estatus` VARCHAR(15) NOT NULL COMMENT '',
  PRIMARY KEY (`id`)  COMMENT '',
  INDEX `fk_CalendarioPagos_1_idx` (`cuenta_id` ASC)  COMMENT '',
  CONSTRAINT `fk_CalendarioPagos_1`
    FOREIGN KEY (`cuenta_id`)
    REFERENCES `podemos_eval`.`Cuentas` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `podemos_eval`.`Clientes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `podemos_eval`.`Clientes` (
  `id` VARCHAR(7) NOT NULL COMMENT '',
  `nombre` VARCHAR(60) NOT NULL COMMENT '',
  PRIMARY KEY (`id`)  COMMENT '')
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `podemos_eval`.`Miembros`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `podemos_eval`.`Miembros` (
  `grupo_id` VARCHAR(5) NOT NULL COMMENT '',
  `cliente_id` VARCHAR(7) NOT NULL COMMENT '',
  PRIMARY KEY (`grupo_id`, `cliente_id`)  COMMENT '',
  INDEX `fk_cliente_idx` (`cliente_id` ASC)  COMMENT '',
  CONSTRAINT `fk_cliente`
    FOREIGN KEY (`cliente_id`)
    REFERENCES `podemos_eval`.`Clientes` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_grupo`
    FOREIGN KEY (`grupo_id`)
    REFERENCES `podemos_eval`.`Grupos` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `podemos_eval`.`Transacciones`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `podemos_eval`.`Transacciones` (
  `id` INT(11) NOT NULL COMMENT '',
  `cuenta_id` VARCHAR(5) NOT NULL COMMENT '',
  `fecha` DATETIME NOT NULL COMMENT '',
  `monto` DECIMAL(15,2) NOT NULL COMMENT '',
  PRIMARY KEY (`id`)  COMMENT '',
  INDEX `fk_Transacciones_1_idx` (`cuenta_id` ASC)  COMMENT '',
  CONSTRAINT `fk_Transacciones_1`
    FOREIGN KEY (`cuenta_id`)
    REFERENCES `podemos_eval`.`Cuentas` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;