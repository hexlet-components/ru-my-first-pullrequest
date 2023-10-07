<?php
use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\Exception;

require 'vendor/autoload.php'; // Путь к файлам PHPMailer

$mail = new PHPMailer(true); // Инициализация PHPMailer с обработкой ошибок

try {
    // Настройки SMTP
    $mail->isSMTP();
    $mail->Host = 'smtp.example.com'; // Укажите адрес SMTP-сервера
    $mail->SMTPAuth = true;
    $mail->Username = 'ваш_адрес@example.com'; // Укажите ваш адрес электронной почты
    $mail->Password = 'ваш_пароль'; // Укажите ваш пароль от почтового ящика
    $mail->SMTPSecure = 'tls'; // Используйте 'tls' или 'ssl' (рекомендуется 'tls')
    $mail->Port = 587; // Порт SMTP-сервера

    // Настройки отправителя и получателя
    $mail->setFrom('ваш_адрес@example.com', 'Ваше Имя');
    $mail->addAddress('получатель@example.com', 'Имя Получателя');

    // Тема и текст письма
    $mail->Subject = 'Тема письма';
    $mail->Body = 'Текст письма';

    // Отправка письма
    $mail->send();
    echo 'Письмо успешно отправлено';
} catch (Exception $e) {
    echo 'Ошибка при отправке письма: ', $mail->ErrorInfo;
}
?>
