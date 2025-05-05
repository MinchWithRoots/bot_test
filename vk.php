<?php
$data = json_decode(file_get_contents('php://input')); 

$confirmation_token = 'f52f1088'; // Этот код который должен получить VK при проверке сервера ставим свои цифры
//Проверяем, что находится в поле "type" 
switch ($data->type) { 
 //Если это уведомление для подтверждения адреса сервера... 
 case 'confirmation': 
 //...отправляем строку для подтверждения адреса 
 echo $confirmation_token; 
 break;
 }
?>
