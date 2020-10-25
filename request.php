<?php

if (is_uploaded_file($_FILES['bill']['tmp_name'])) {
    $uploads_dir = '/home/hubert/Documents/Projects/BESTHacksTest/data/testing/';
    $tmp_name = $_FILES['bill']['tmp_name'];
    $pic_name = $_FILES['bill']['name'];
    move_uploaded_file($tmp_name, $uploads_dir.$pic_name.".jpg");

    shell_exec("convert /home/hubert/Documents/Projects/BESTHacksTest/data/testing/image.jpg -resize 300 /home/hubert/Documents/Projects/BESTHacksTest/data/testing/imageSmall.jpg");
    $path = '/home/hubert/Documents/Projects/BESTHacksTest/data/testing/image.jpg';
    unlink($path);
    $output = shell_exec("python3 /home/hubert/Documents/Projects/BESTHacksTest/main.py");
    echo($output);
}
else {
    print("-1");
}
?>
