<?php
    $query = $argv[1];
    srand(mktime());
    $choice=(rand(2,10));
    
    
    switch ($choice) {
    case 2:
        $useragent = 'Mozilla/5.0 (Windows NT 5.1; rv:31.0) Gecko/20100101 Firefox/31.0';//"Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.14912/870; U; id) Presto/2.4.15";
        break;
//         echo '2';
    case 3:
        $useragent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.104 Safari/537.36';
//         echo '3';
        break;
    case 4:
        $useragent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36';
//         echo "i equals 4";
        break;
    case 5:
        $useragent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10) AppleWebKit/600.1.25 (KHTML, like Gecko) Version/8.0 Safari/600.1.25';
//         echo "i equals 5";
        break;
    case 6:
        $useragent= 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko';
//         echo "i equals 6";
        break;
    case 7:
        $useragent= 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36'; //chrom 38 on win7
//         echo "i equals 7";
        break;
    case 8:
        $useragent= 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.65 Safari/537.36';
//         echo "i equals 8";
        break;
    case 9:
        $useragent='Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36';
//         echo "i equals 9";
        break;
    case 10:
        $useragent='Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)';
//         echo "i equals 10";
        break;       
}
    
        

    $ch = curl_init ("");
    curl_setopt ($ch, CURLOPT_URL, "http://www.google.com/search?q=".$query);
    curl_setopt ($ch, CURLOPT_USERAGENT, $useragent); // set user agent
    curl_setopt ($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_FOLLOWLOCATION, TRUE);
    $output = curl_exec($ch);
    file_put_contents("google.html",$output);
    curl_close($ch);
    echo $useragent;
     //echo $choice;
?>