import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from tabulate import tabulate
import csv
import pandas as pd
#url of the page we want to scrape
url = "https://saluddigital.ssch.gob.mx/covid/"

# initiating the webdriver. Parameter includes the path of the webdriver.
driver = webdriver.Chrome()
driver.get(url)
time.sleep(5) # delay for load properly
# # this is just to ensure that the page is loaded
html = driver.page_source
html = """<html xmlns="http://www.w3.org/1999/xhtml" class="ui-mobile"><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>Salud Digital</title><link href="https://fonts.googleapis.com/css?family=Roboto&amp;display=swap" rel="stylesheet"><link href="https://fonts.googleapis.com/css?family=Righteous|Roboto&amp;display=swap" rel="stylesheet"><link href="https://fonts.googleapis.com/css?family=Open+Sans&amp;display=swap" rel="stylesheet"><link href="../Assets/fontawesome/css/all.css" rel="stylesheet" type="text/css"><meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no"><meta charset="utf-8"><link id="ctl00_ln_favicon" rel="shortcut icon" href="./assets/images/icono.png"><meta http-equiv="X-UA-Compatible" content="IE=edge"><meta http-equiv="Content-Language" content="es"><link id="ctl00_general_css" href="../app/css/v-1003/movil_v1.css?v=100" rel="stylesheet" type="text/css"><link id="ctl00_covid_css" href="/covid/css/v-1003/cssPC.css?v=100" rel="stylesheet" type="text/css"><link href="../app/css/Starraking.css?v=23" rel="stylesheet" type="text/css"><link href="../Assets/Select2/select2.min.css?v=21" rel="stylesheet" type="text/css"><link href="../Assets/chosen/chosen.css?v=21" rel="stylesheet" type="text/css"><meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <script src="/app/js/jquery.min.js" type="text/javascript"></script>
    <script src="/Assets/jquery.mobile.js" type="text/javascript"></script>
    <script src="/Assets/qrcode.js" type="text/javascript"></script>
    <script src="/Assets/jquery.maskedinput.js" type="text/javascript"></script>
    <script src="/Assets/Select2/select2.min.js" type="text/javascript"></script>
    <script src="/Assets/chosen/chosen.jquery.js" type="text/javascript"></script>
    <script src="/Assets/qrcode.js" type="text/javascript"></script>

    <script>
        var _ios_vercion = -1;
        function returnVersion(versiones) {
            _ios_vercion = versiones;
            $("#vercion_test2").html(versiones);
        }
    </script>

    <script type="text/javascript" src="/app/js/v-1002/geolocation_v1.js?v=45"></script>
<!-- ADVERTENCIA: , ERROR: EL BUNDLE app/js/v-1002/geolocation_v1.js NO EXISTE --><script type="text/javascript" src="/app/js/Base64.js?v=22"></script>
<!-- ADVERTENCIA: , ERROR: EL BUNDLE app/js/Base64.js NO EXISTE --><script type="text/javascript" src="/covid/js/sha1.js?v=22"></script>
<!-- ADVERTENCIA: , ERROR: EL BUNDLE covid/js/sha1.js NO EXISTE --><script type="text/javascript" src="/app/js/v-1002/so_comunes.js?v=30"></script>
<!-- ADVERTENCIA: , ERROR: EL BUNDLE app/js/v-1002/so_comunes.js NO EXISTE --><script type="text/javascript" src="/covid/js/v-1002/alerta.js?v=23"></script>
<!-- ADVERTENCIA: , ERROR: EL BUNDLE covid/js/v-1002/alerta.js NO EXISTE --><script type="text/javascript" src="/app/js/starraking.js?v=29"></script>
<!-- ADVERTENCIA: , ERROR: EL BUNDLE app/js/starraking.js NO EXISTE -->
      <script type="text/javascript" src="/covid/js/v-1002/default_v5.js?v=4"></script>
<!-- ADVERTENCIA: , ERROR: EL BUNDLE covid/js/v-1002/default_v5.js NO EXISTE -->
    <link href="../covid/css/cssNoticias_v3.css?v=220" rel="stylesheet" type="text/css">
    <script>
        $(document).ready(function () {
            var acces = getParameterByName("acces");
            var slide = 1;
            var max_slide = 4;

            $(".sp_atras").click(function () {
                window.location.href = $("#hd_raiz").html() + "covid/caso.aspx?acces=" + acces;
            });

            $("meta[name='viewport']").attr("content", "width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no");
            $("#ctl00_covid_css").attr("href", $("#hd_raiz").html() + "covid/css/v-1002/cssAndroid_v1.css?v=4");

            setInterval(function () {
                let slide_actual = slide;
                slide++;
                if (slide > max_slide) {
                    slide = 1;
                }
                $("#lamina" + slide_actual).fadeOut(700);
                setTimeout(
                    function () {
                        $("#lamina" + slide).fadeIn("slow");
                    }, 700);
               

                $(".boton").removeClass("boton-activo");
                $("#btn" + slide).addClass("boton-activo");

            }, 4000);


            $(document).on("click", ".caja-noticia", function () {
                $(".caja-noticia").fadeOut("slow");
                var id = $(this).data("noticia");
                $("#noti" + id).fadeIn("slow");
            });

            $(document).on("click", ".cerrar-noticia", function () {
                $(".noticia-cuerpo").fadeOut("slow");
                $(".caja-noticia").fadeIn("slow");
            });

            CargaDatosNoticias = function () {
                $.ajax({
                    type: 'GET',
                    url: $("#hd_raiz").html() + 'app/Asincronos/_covid.ashx',
                    data: {
                        accion: "lstnoticia"
                    },
                    error: function (err) {
                        alert(err.statusCode);
                    },
                    success: function (resp) {
                        var datos = CreaArreglo(resp, "??", "??");
                        DibujaNoticia(datos);
                    }

                });
            }

            DibujaNoticia = function (datos) {
                var html = "";
                for (var i = 0; i < datos.length; i++) {
                    if (datos[i].length > 1) {
                        html += `
                              <div class="caja-noticia" data-noticia="${i}">
                    <h2>${datos[i][0]}</h2>
                    <img src="${datos[i][1]}" />
                </div>
                <div class="noticia-cuerpo" id="noti${i}" style="display: none;">
                    <div class="cerrar-noticia"> <i class="fad fa-arrow-circle-left"></i>  Atr??s</div>
                    <img src="${datos[i][1]}" />
                    <h1>${datos[i][0]}</h1>
                    <div class="content-inner">
                            ${datos[i][2]}
                          </div>
                </div>
                        `;
                    }
                }
                $(".noticias-contgenedor").html(html);
            }
            CargaDatosTabla = function () {
                $.ajax({
                    type: 'GET',
                    url: $("#hd_raiz").html() + 'app/asincronos/jsonstats.ashx?getconteos=1',
                    data: {
                        //accion: "lstnoticia"
                    },
                    error: function (err) {
                        alert(err.statusCode);
                    },
                    success: function (resp) {
                        

                        var datos = resp.data;

                        var html = `<table class="casos"  cellpadding="0" cellspacing="0">
                            <tr class="header-table">
                                <td>Semaforo</td>
                                <td>Lugar</td>
                                <td>Confirmados</td>
                                <td>Sospechosos</td>
                                <td>Descartados</td>
                                <td>Recuperados</td>
                                <td>Defunciones</td>
                            </tr>`;

                        var ringlo = 1;

                        for (var i = 0; i < datos.length; i++) {
                            var recuperados = datos[i].value.recuperados;
                            if (recuperados == undefined) {
                                recuperados = "-";
                            }

                            html += `
                                <tr class="ringlon-${ringlo}">
                                    <td class="semaforo">${(datos[i].value.semaforo == undefined) ? '' : datos[i].value.semaforo}</td>
                                    <td>${datos[i].value.lugar}</td>
                                    <td>${datos[i].value.confirmados}</td>
                                    <td>${datos[i].value.sospechosos}</td>
                                    <td>${datos[i].value.descartados}</td>
                                    <td>${recuperados}</td>
                                    <td>${datos[i].value.defunciones}</td>
                                </tr>
                                `;
                            if (ringlo == 1) {
                                ringlo = 2;
                            } else {
                                ringlo = 1;
                            }
                        }
                        html += "</table>";
                        $(".contenedor-general").html(html);
                        $(".semaforo img").each(function () {
                            $(this).attr("width", "20");
                        });
                        var d = new Date();
                        $("#fechahora").html("Corte: " + FormatoADosCifras(d.getDate()) + " de " +
                            numero_letra_mes(FormatoADosCifras(d.getMonth() + 1)) + " del 2020, 8:00 AM");
                    }

                });
            }


            $("#btn_plan").click(function () {
                window.location.href = $("#hd_raiz").html() + "covid/plan.aspx?acces=" + acces + "&ori=2";
            });

            $("#btn_videos").click(function () {
                window.location.href = $("#hd_raiz").html() + "covid/videos.aspx?acces=" + acces + "&ori=2";
            });


            $("#contadores_empresas").click(function () {
                window.location.href = $("#hd_raiz").html() + "panel/empresas.aspx?sd=1";
            });

            CargaDatosNoticias();
            CargaDatosTabla();

        });
    </script>
     <style>
        .footer-bar {
            height: 26px;
            background-color: #2D5F8B;
            color: white;
            display: flex;
            justify-content: center;
            align-items: center;
            position: FIXED;
            width: 100%;
            bottom: 0;
            left: 0;
            font-size: 17px;
        }

        .sp_atras {
            position: absolute;
            font-size: 33px;
            left: 0px;
            top: 0;
            height: 50px;
            width: 50px;
            display: flex;
            justify-content: center;
            align-items: center;
        }
    </style>


    <script>
        $(document).ready(function () {
            var header_height = 240;
            var href = $(location).attr('href');


            if (EsMobil() == "Android" || EsMobil() == "PC" || href.indexOf("informacion") != -1) {
                header_height = 100;
            }

           
            $("#header_falso").attr("style", "height: " + header_height + "px;");


            if (EsMobil() == "Android") {
                $("meta[name='viewport']").attr("content", "width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no");
                $("#ctl00_covid_css").attr("href", $("#hd_raiz").html() + "covid/css/v-1003/cssAndroid_v1.css?v=100");
            } else {
                if (EsMobil() == "PC") {
                    $("meta[name='viewport']").attr("content", "width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no");
                    $("#ctl00_covid_css").attr("href", $("#hd_raiz").html() + "covid/css/v-1003/cssPC.css?v=100");
                }
            }
            //Esto

            $('#se').on('load', function () {
                $(this).contents().find("img").css({ 'width': '100%', 'height': 'auto' });
            });

            $(".closs-visor").click(function () {
                $(".visor-imagen").addClass("hide");
            });
            const x = sha256('6144963144');
            console.log(x);

            //function returnVersion(versiones) {
            //    document.getElementById("mitoken").value = versiones;
            //}
            //function version() {
            //    try {
            //        webkit.messageHandlers.getVersion.postMessage("");
            //    } catch (err) { console.log('The native context does not exist yet'); }
            //}
            
            //version();

        });
    </script>
</head>
<body class="ui-pagecontainer ui-mobile-viewport ui-overlay-a"><div data-role="page" data-url="/covid/" tabindex="0" class="ui-page ui-page-theme-a ui-page-active" style="">
    <div class="sw-error-box" style="display: none;"><b>
        <i class="fas fa-exclamation"></i>Error: </b><span class="sp_mensaje_error_box"></span>
    </div>

    <div class="opaco-cargando" style="display: none;">
        <img src="/app/img/movil-load.gif" style="width: 100%">
    </div>
     <div class="opaco-mensjae" id="mensaje_alerta" style="display: none;">
        <p><span id="tienda-mensaje">Est??s usando una versi??n antigua de la aplicaci??n, por favor descarga la ??ltima versi??n desde la </span> <span id="tienda"></span></p>
        <div class="btn" id="btn_aceptar_tienda">Aceptar</div>
    </div>

    <div class="opaco-menu hide"></div>
    <div class="visor-imagen hide">
        <div class="closs-visor"><i class="fal fa-times"></i></div>
        <iframe src="img/inicio.jpeg" id="se" style="width: 80%; margin-left: 10%; height: 70%; margin-top: 15%;"></iframe>
    </div>

    <div class="header-bar barra-covid" style="height: auto; display: block;">
        <img src="img/logo.png">
        <span class="sp_logo">
            <h1 id="h_titulo">SALUD DIGITAL</h1>
            <h2>COVID-19</h2>
        </span>
        <br style="clear: left;">
    </div>
    <div id="header_falso" class="header-bar" style="height: 100px;">
        <br style="clear: left;">
        <br style="clear: left;">
        <br style="clear: left;">
        <br style="clear: left;">
        <br style="clear: left;">

    </div>
     <br style="clear: left;">
    <div id="cuerpo">
        
       <span class="pc-columna-right">
    <div class="btn hide" id="btn_registrar" style="height: auto;
    text-align: center;
    margin-top: 15px;
    font-size: 20px;
    margin-bottom: 20px;
    width: 78% !important;">
                Reg??strate y averigua si eres sospechoso de COVID-19
    </div>


         </span>
    <span class="pc-columna-left">
        <div id="contenador">
        <div class="platilla-Titulo">Situaci??n Actual</div>
        <div class="contenedor-general"><table class="casos" cellpadding="0" cellspacing="0">
                            <tbody><tr class="header-table">
                                <td>Semaforo</td>
                                <td>Lugar</td>
                                <td>Confirmados</td>
                                <td>Sospechosos</td>
                                <td>Descartados</td>
                                <td>Recuperados</td>
                                <td>Defunciones</td>
                            </tr>
                                <tr class="ringlon-1">
                                    <td class="semaforo"><img src="https://comunicachihuahua.desarrollosenlanube.net/wp-content/uploads/2020/06/semaforoNaranja.png" alt="" width="20" height="20" class="alignnone size-full wp-image-6132"></td>
                                    <td><strong>Estatal</strong></td>
                                    <td>42231</td>
                                    <td>2859</td>
                                    <td>21864</td>
                                    <td>23550</td>
                                    <td>3975</td>
                                </tr>
                                
                                <tr class="ringlon-2">
                                    <td class="semaforo"><img src="https://comunicachihuahua.desarrollosenlanube.net/wp-content/uploads/2020/06/semaforoNaranja.png" alt="" width="20" height="20" class="alignnone size-full wp-image-6132"></td>
                                    <td>Ju??rez</td>
                                    <td>23877</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>2318</td>
                                </tr>
                                
                                <tr class="ringlon-1">
                                    <td class="semaforo"><img src="https://comunicachihuahua.desarrollosenlanube.net/wp-content/uploads/2020/06/semaforoNaranja.png" alt="" width="20" height="20" class="alignnone size-full wp-image-6132"></td>
                                    <td>Chihuahua</td>
                                    <td>9654</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>798</td>
                                </tr>
                                
                                <tr class="ringlon-2">
                                    <td class="semaforo"><img src="https://comunicachihuahua.desarrollosenlanube.net/wp-content/uploads/2020/06/semaforoNaranja.png" alt="" width="20" height="20" class="alignnone size-full wp-image-6132"></td>
                                    <td>Delicias</td>
                                    <td>1634</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>192</td>
                                </tr>
                                
                                <tr class="ringlon-1">
                                    <td class="semaforo"><img src="https://comunicachihuahua.desarrollosenlanube.net/wp-content/uploads/2020/06/semaforoNaranja.png" alt="" width="20" height="20" class="alignnone size-full wp-image-6132"></td>
                                    <td>Parral</td>
                                    <td>1517</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>144</td>
                                </tr>
                                
                                <tr class="ringlon-2">
                                    <td class="semaforo"><img src="https://comunicachihuahua.desarrollosenlanube.net/wp-content/uploads/2020/06/semaforoNaranja.png" alt="" width="20" height="20" class="alignnone size-full wp-image-6132"></td>
                                    <td>Cuauht??moc</td>
                                    <td>1314</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>125</td>
                                </tr>
                                
                                <tr class="ringlon-1">
                                    <td class="semaforo"><img src="https://comunicachihuahua.desarrollosenlanube.net/wp-content/uploads/2020/06/semaforoNaranja.png" alt="" width="20" height="20" class="alignnone size-full wp-image-6132"></td>
                                    <td>Ojinaga</td>
                                    <td>763</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>8</td>
                                </tr>
                                
                                <tr class="ringlon-2">
                                    <td class="semaforo"><img src="https://comunicachihuahua.desarrollosenlanube.net/wp-content/uploads/2020/06/semaforoNaranja.png" alt="" width="20" height="20" class="alignnone size-full wp-image-6132"></td>
                                    <td>Nuevo Casas Grandes</td>
                                    <td>634</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>55</td>
                                </tr>
                                
                                <tr class="ringlon-1">
                                    <td class="semaforo"><img src="https://comunicachihuahua.desarrollosenlanube.net/wp-content/uploads/2020/06/semaforoNaranja.png" alt="" width="20" height="20" class="alignnone size-full wp-image-6132"></td>
                                    <td>Camargo</td>
                                    <td>289</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>39</td>
                                </tr>
                                
                                <tr class="ringlon-2">
                                    <td class="semaforo"><img src="https://comunicachihuahua.desarrollosenlanube.net/wp-content/uploads/2020/06/semaforoNaranja.png" alt="" width="20" height="20" class="alignnone size-full wp-image-6132"></td>
                                    <td>Bocoyna</td>
                                    <td>272</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>7</td>
                                </tr>
                                
                                <tr class="ringlon-1">
                                    <td class="semaforo"><img src="https://comunicachihuahua.desarrollosenlanube.net/wp-content/uploads/2020/06/semaforoNaranja.png" alt="" width="20" height="20" class="alignnone size-full wp-image-6132"></td>
                                    <td>Guachochi</td>
                                    <td>233</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>14</td>
                                </tr>
                                
                                <tr class="ringlon-2">
                                    <td class="semaforo"><img src="https://comunicachihuahua.desarrollosenlanube.net/wp-content/uploads/2020/06/semaforoNaranja.png" alt="" width="20" height="20" class="alignnone size-full wp-image-6132"></td>
                                    <td>Meoqui</td>
                                    <td>222</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>43</td>
                                </tr>
                                
                                <tr class="ringlon-1">
                                    <td class="semaforo"><img src="https://comunicachihuahua.desarrollosenlanube.net/wp-content/uploads/2020/06/semaforoNaranja.png" alt="" width="20" height="20" class="alignnone size-full wp-image-6132"></td>
                                    <td>Jimenez</td>
                                    <td>191</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>20</td>
                                </tr>
                                
                                <tr class="ringlon-2">
                                    <td class="semaforo"><img src="https://comunicachihuahua.desarrollosenlanube.net/wp-content/uploads/2020/06/semaforoNaranja.png" alt="" width="20" height="20" class="alignnone size-full wp-image-6132"></td>
                                    <td>Saucillo</td>
                                    <td>171</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>33</td>
                                </tr>
                                
                                <tr class="ringlon-1">
                                    <td class="semaforo"><img src="https://comunicachihuahua.desarrollosenlanube.net/wp-content/uploads/2020/06/semaforoNaranja.png" alt="" width="20" height="20" class="alignnone size-full wp-image-6132"></td>
                                    <td>Aquiles Serd??n</td>
                                    <td>152</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>7</td>
                                </tr>
                                
                                <tr class="ringlon-2">
                                    <td class="semaforo"><img src="https://comunicachihuahua.desarrollosenlanube.net/wp-content/uploads/2020/06/semaforoNaranja.png" alt="" width="20" height="20" class="alignnone size-full wp-image-6132"></td>
                                    <td>Chinipas</td>
                                    <td>115</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>-</td>
                                </tr>
                                
                                <tr class="ringlon-1">
                                    <td class="semaforo"><img src="https://comunicachihuahua.desarrollosenlanube.net/wp-content/uploads/2020/06/semaforoNaranja.png" alt="" width="20" height="20" class="alignnone size-full wp-image-6132"></td>
                                    <td>Aldama</td>
                                    <td>98</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>7</td>
                                </tr>
                                
                                <tr class="ringlon-2">
                                    <td class="semaforo"><img src="https://comunicachihuahua.desarrollosenlanube.net/wp-content/uploads/2020/06/semaforoNaranja.png" alt="" width="20" height="20" class="alignnone size-full wp-image-6132"></td>
                                    <td>Ahumada</td>
                                    <td>77</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>9</td>
                                </tr>
                                
                                <tr class="ringlon-1">
                                    <td class="semaforo"><img src="https://comunicachihuahua.desarrollosenlanube.net/wp-content/uploads/2020/06/semaforoNaranja.png" alt="" width="20" height="20" class="alignnone size-full wp-image-6132"></td>
                                    <td>Allende</td>
                                    <td>72</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>2</td>
                                </tr>
                                
                                <tr class="ringlon-2">
                                    <td class="semaforo"><img src="https://comunicachihuahua.desarrollosenlanube.net/wp-content/uploads/2020/06/semaforoNaranja.png" alt="" width="20" height="20" class="alignnone size-full wp-image-6132"></td>
                                    <td>G??mez Far??as</td>
                                    <td>68</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>4</td>
                                </tr>
                                
                                <tr class="ringlon-1">
                                    <td class="semaforo"><img src="https://comunicachihuahua.desarrollosenlanube.net/wp-content/uploads/2020/06/semaforoNaranja.png" alt="" width="20" height="20" class="alignnone size-full wp-image-6132"></td>
                                    <td>Namiquipa</td>
                                    <td>67</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>6</td>
                                </tr>
                                
                                <tr class="ringlon-2">
                                    <td class="semaforo"><img src="https://comunicachihuahua.desarrollosenlanube.net/wp-content/uploads/2020/06/semaforoNaranja.png" alt="" width="20" height="20" class="alignnone size-full wp-image-6132"></td>
                                    <td>Guazapares</td>
                                    <td>66</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>1</td>
                                </tr>
                                
                                <tr class="ringlon-1">
                                    <td class="semaforo"><img src="https://comunicachihuahua.desarrollosenlanube.net/wp-content/uploads/2020/06/semaforoNaranja.png" alt="" width="20" height="20" class="alignnone size-full wp-image-6132"></td>
                                    <td>Ascensi??n</td>
                                    <td>64</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>12</td>
                                </tr>
                                
                                <tr class="ringlon-2">
                                    <td class="semaforo"><img src="https://comunicachihuahua.desarrollosenlanube.net/wp-content/uploads/2020/06/semaforoNaranja.png" alt="" width="20" height="20" class="alignnone size-full wp-image-6132"></td>
                                    <td>Guerrero</td>
                                    <td>60</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>19</td>
                                </tr>
                                
                                <tr class="ringlon-1">
                                    <td class="semaforo"><img src="https://comunicachihuahua.desarrollosenlanube.net/wp-content/uploads/2020/06/semaforoNaranja.png" alt="" width="20" height="20" class="alignnone size-full wp-image-6132"></td>
                                    <td>Santa B??rbara</td>
                                    <td>60</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>5</td>
                                </tr>
                                
                                <tr class="ringlon-2">
                                    <td class="semaforo"><img src="https://comunicachihuahua.desarrollosenlanube.net/wp-content/uploads/2020/06/semaforoNaranja.png" alt="" width="20" height="20" class="alignnone size-full wp-image-6132"></td>
                                    <td>Rosales</td>
                                    <td>59</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>11</td>
                                </tr>
                                
                                <tr class="ringlon-1">
                                    <td class="semaforo"><img src="https://comunicachihuahua.desarrollosenlanube.net/wp-content/uploads/2020/06/semaforoNaranja.png" alt="" width="20" height="20" class="alignnone size-full wp-image-6132"></td>
                                    <td>Urique</td>
                                    <td>37</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>4</td>
                                </tr>
                                
                                <tr class="ringlon-2">
                                    <td class="semaforo"><img src="https://comunicachihuahua.desarrollosenlanube.net/wp-content/uploads/2020/06/semaforoNaranja.png" alt="" width="20" height="20" class="alignnone size-full wp-image-6132"></td>
                                    <td>Madera</td>
                                    <td>35</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>8</td>
                                </tr>
                                
                                <tr class="ringlon-1">
                                    <td class="semaforo"><img src="https://comunicachihuahua.desarrollosenlanube.net/wp-content/uploads/2020/06/semaforoNaranja.png" alt="" width="20" height="20" class="alignnone size-full wp-image-6132"></td>
                                    <td>Buenaventura</td>
                                    <td>34</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>7</td>
                                </tr>
                                
                                <tr class="ringlon-2">
                                    <td class="semaforo"><img src="https://comunicachihuahua.desarrollosenlanube.net/wp-content/uploads/2020/06/semaforoNaranja.png" alt="" width="20" height="20" class="alignnone size-full wp-image-6132"></td>
                                    <td>Guadalupe y Calvo</td>
                                    <td>28</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>2</td>
                                </tr>
                                
                                <tr class="ringlon-1">
                                    <td class="semaforo"><img src="https://comunicachihuahua.desarrollosenlanube.net/wp-content/uploads/2020/06/semaforoNaranja.png" alt="" width="20" height="20" class="alignnone size-full wp-image-6132"></td>
                                    <td>Manuel Benavides</td>
                                    <td>25</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>-</td>
                                </tr>
                                
                                <tr class="ringlon-2">
                                    <td class="semaforo"><img src="https://comunicachihuahua.desarrollosenlanube.net/wp-content/uploads/2020/06/semaforoNaranja.png" alt="" width="20" height="20" class="alignnone size-full wp-image-6132"></td>
                                    <td>Casas Grandes</td>
                                    <td>24</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>5</td>
                                </tr>
                                
                                <tr class="ringlon-1">
                                    <td class="semaforo"><img src="https://comunicachihuahua.desarrollosenlanube.net/wp-content/uploads/2020/06/semaforoNaranja.png" alt="" width="20" height="20" class="alignnone size-full wp-image-6132"></td>
                                    <td>Sn. Fco del Oro</td>
                                    <td>23</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>6</td>
                                </tr>
                                
                                <tr class="ringlon-2">
                                    <td class="semaforo"><img src="https://comunicachihuahua.desarrollosenlanube.net/wp-content/uploads/2020/06/semaforoNaranja.png" alt="" width="20" height="20" class="alignnone size-full wp-image-6132"></td>
                                    <td>La Cruz</td>
                                    <td>21</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>-</td>
                                </tr>
                                
                                <tr class="ringlon-1">
                                    <td class="semaforo"><img src="https://comunicachihuahua.desarrollosenlanube.net/wp-content/uploads/2020/06/semaforoNaranja.png" alt="" width="20" height="20" class="alignnone size-full wp-image-6132"></td>
                                    <td>Janos</td>
                                    <td>20</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>3</td>
                                </tr>
                                
                                <tr class="ringlon-2">
                                    <td class="semaforo"><img src="https://comunicachihuahua.desarrollosenlanube.net/wp-content/uploads/2020/06/semaforoNaranja.png" alt="" width="20" height="20" class="alignnone size-full wp-image-6132"></td>
                                    <td>Nonoava</td>
                                    <td>17</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>2</td>
                                </tr>
                                
                                <tr class="ringlon-1">
                                    <td class="semaforo"><img src="https://comunicachihuahua.desarrollosenlanube.net/wp-content/uploads/2020/06/semaforoNaranja.png" alt="" width="20" height="20" class="alignnone size-full wp-image-6132"></td>
                                    <td>Ocampo</td>
                                    <td>15</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>4</td>
                                </tr>
                                
                                <tr class="ringlon-2">
                                    <td class="semaforo"><img src="https://comunicachihuahua.desarrollosenlanube.net/wp-content/uploads/2020/06/semaforoNaranja.png" alt="" width="20" height="20" class="alignnone size-full wp-image-6132"></td>
                                    <td>Bachiniva</td>
                                    <td>14</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>1</td>
                                </tr>
                                
                                <tr class="ringlon-1">
                                    <td class="semaforo"><img src="https://comunicachihuahua.desarrollosenlanube.net/wp-content/uploads/2020/06/semaforoNaranja.png" alt="" width="20" height="20" class="alignnone size-full wp-image-6132"></td>
                                    <td>Guadalupe</td>
                                    <td>14</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>3</td>
                                </tr>
                                
                                <tr class="ringlon-2">
                                    <td class="semaforo"><img src="https://comunicachihuahua.desarrollosenlanube.net/wp-content/uploads/2020/06/semaforoNaranja.png" alt="" width="20" height="20" class="alignnone size-full wp-image-6132"></td>
                                    <td>Matamoros</td>
                                    <td>14</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>-</td>
                                </tr>
                                
                                <tr class="ringlon-1">
                                    <td class="semaforo"><img src="https://comunicachihuahua.desarrollosenlanube.net/wp-content/uploads/2020/06/semaforoNaranja.png" alt="" width="20" height="20" class="alignnone size-full wp-image-6132"></td>
                                    <td>Cusihuiriachi</td>
                                    <td>13</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>3</td>
                                </tr>
                                
                                <tr class="ringlon-2">
                                    <td class="semaforo"><img src="https://comunicachihuahua.desarrollosenlanube.net/wp-content/uploads/2020/06/semaforoNaranja.png" alt="" width="20" height="20" class="alignnone size-full wp-image-6132"></td>
                                    <td>Santa Isabel</td>
                                    <td>13</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>1</td>
                                </tr>
                                
                                <tr class="ringlon-1">
                                    <td class="semaforo"><img src="https://comunicachihuahua.desarrollosenlanube.net/wp-content/uploads/2020/06/semaforoNaranja.png" alt="" width="20" height="20" class="alignnone size-full wp-image-6132"></td>
                                    <td>Ignacio Zaragoza</td>
                                    <td>12</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>3</td>
                                </tr>
                                
                                <tr class="ringlon-2">
                                    <td class="semaforo"><img src="https://comunicachihuahua.desarrollosenlanube.net/wp-content/uploads/2020/06/semaforoNaranja.png" alt="" width="20" height="20" class="alignnone size-full wp-image-6132"></td>
                                    <td>Valle de Zaragoza</td>
                                    <td>12</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>2</td>
                                </tr>
                                
                                <tr class="ringlon-1">
                                    <td class="semaforo"><img src="https://comunicachihuahua.desarrollosenlanube.net/wp-content/uploads/2020/06/semaforoNaranja.png" alt="" width="20" height="20" class="alignnone size-full wp-image-6132"></td>
                                    <td>Praxedis G.
Guerrero</td>
                                    <td>11</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>-</td>
                                </tr>
                                
                                <tr class="ringlon-2">
                                    <td class="semaforo"><img src="https://comunicachihuahua.desarrollosenlanube.net/wp-content/uploads/2020/06/semaforoNaranja.png" alt="" width="20" height="20" class="alignnone size-full wp-image-6132"></td>
                                    <td>San Francisco de Conchos</td>
                                    <td>11</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>3</td>
                                </tr>
                                
                                <tr class="ringlon-1">
                                    <td class="semaforo"><img src="https://comunicachihuahua.desarrollosenlanube.net/wp-content/uploads/2020/06/semaforoNaranja.png" alt="" width="20" height="20" class="alignnone size-full wp-image-6132"></td>
                                    <td>Julimes
</td>
                                    <td>9</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>4</td>
                                </tr>
                                
                                <tr class="ringlon-2">
                                    <td class="semaforo"><img src="https://comunicachihuahua.desarrollosenlanube.net/wp-content/uploads/2020/06/semaforoNaranja.png" alt="" width="20" height="20" class="alignnone size-full wp-image-6132"></td>
                                    <td>Temosachic</td>
                                    <td>9</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>5</td>
                                </tr>
                                
                                <tr class="ringlon-1">
                                    <td class="semaforo"><img src="https://comunicachihuahua.desarrollosenlanube.net/wp-content/uploads/2020/06/semaforoNaranja.png" alt="" width="20" height="20" class="alignnone size-full wp-image-6132"></td>
                                    <td>Balleza</td>
                                    <td>9</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>2</td>
                                </tr>
                                
                                <tr class="ringlon-2">
                                    <td class="semaforo"><img src="https://comunicachihuahua.desarrollosenlanube.net/wp-content/uploads/2020/06/semaforoNaranja.png" alt="" width="20" height="20" class="alignnone size-full wp-image-6132"></td>
                                    <td>Gran Morelos</td>
                                    <td>9</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>1</td>
                                </tr>
                                
                                <tr class="ringlon-1">
                                    <td class="semaforo"><img src="https://comunicachihuahua.desarrollosenlanube.net/wp-content/uploads/2020/06/semaforoNaranja.png" alt="" width="20" height="20" class="alignnone size-full wp-image-6132"></td>
                                    <td>Carichi</td>
                                    <td>8</td>
                                    <td></td>
                                    <td></td>
                                    <td>-</td>
                                    <td>5</td>
                                </tr>
                                
                                <tr class="ringlon-2">
                                    <td class="semaforo"><img src="https://comunicachihuahua.desarrollosenlanube.net/wp-content/uploads/2020/06/semaforoNaranja.png" alt="" width="20" height="20" class="alignnone size-full wp-image-6132"></td>
                                    <td>Coyame del Sotol</td>
                                    <td>8</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>3</td>
                                </tr>
                                
                                <tr class="ringlon-1">
                                    <td class="semaforo"><img src="https://comunicachihuahua.desarrollosenlanube.net/wp-content/uploads/2020/06/semaforoNaranja.png" alt="" width="20" height="20" class="alignnone size-full wp-image-6132"></td>
                                    <td>Lopez</td>
                                    <td>8</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>3</td>
                                </tr>
                                
                                <tr class="ringlon-2">
                                    <td class="semaforo"><img src="https://comunicachihuahua.desarrollosenlanube.net/wp-content/uploads/2020/06/semaforoNaranja.png" alt="" width="20" height="20" class="alignnone size-full wp-image-6132"></td>
                                    <td>Galeana</td>
                                    <td>7</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>4</td>
                                </tr>
                                
                                <tr class="ringlon-1">
                                    <td class="semaforo"><img src="https://comunicachihuahua.desarrollosenlanube.net/wp-content/uploads/2020/06/semaforoNaranja.png" alt="" width="20" height="20" class="alignnone size-full wp-image-6132"></td>
                                    <td>La Cruz</td>
                                    <td>7</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>-</td>
                                </tr>
                                
                                <tr class="ringlon-2">
                                    <td class="semaforo"><img src="https://comunicachihuahua.desarrollosenlanube.net/wp-content/uploads/2020/06/semaforoNaranja.png" alt="" width="20" height="20" class="alignnone size-full wp-image-6132"></td>
                                    <td>Batopilas</td>
                                    <td>6</td>
                                    <td></td>
                                    <td></td>
                                    <td>-</td>
                                    <td>-</td>
                                </tr>
                                
                                <tr class="ringlon-1">
                                    <td class="semaforo"><img src="https://comunicachihuahua.desarrollosenlanube.net/wp-content/uploads/2020/06/semaforoNaranja.png" alt="" width="20" height="20" class="alignnone size-full wp-image-6132"></td>
                                    <td>Riva Palacio</td>
                                    <td>6</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>3</td>
                                </tr>
                                
                                <tr class="ringlon-2">
                                    <td class="semaforo"><img src="https://comunicachihuahua.desarrollosenlanube.net/wp-content/uploads/2020/06/semaforoNaranja.png" alt="" width="20" height="20" class="alignnone size-full wp-image-6132"></td>
                                    <td>San Francisco de Borja</td>
                                    <td>5</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>-</td>
                                </tr>
                                
                                <tr class="ringlon-1">
                                    <td class="semaforo"><img src="https://comunicachihuahua.desarrollosenlanube.net/wp-content/uploads/2020/06/semaforoNaranja.png" alt="" width="20" height="20" class="alignnone size-full wp-image-6132"></td>
                                    <td>Coronado</td>
                                    <td>5</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>3</td>
                                </tr>
                                
                                <tr class="ringlon-2">
                                    <td class="semaforo"><img src="https://comunicachihuahua.desarrollosenlanube.net/wp-content/uploads/2020/06/semaforoNaranja.png" alt="" width="20" height="20" class="alignnone size-full wp-image-6132"></td>
                                    <td>Satevo</td>
                                    <td>5</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>-</td>
                                </tr>
                                
                                <tr class="ringlon-1">
                                    <td class="semaforo"><img src="https://comunicachihuahua.desarrollosenlanube.net/wp-content/uploads/2020/06/semaforoNaranja.png" alt="" width="20" height="20" class="alignnone size-full wp-image-6132"></td>
                                    <td>El Tule</td>
                                    <td>4</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>1</td>
                                </tr>
                                
                                <tr class="ringlon-2">
                                    <td class="semaforo"><img src="https://comunicachihuahua.desarrollosenlanube.net/wp-content/uploads/2020/06/semaforoNaranja.png" alt="" width="20" height="20" class="alignnone size-full wp-image-6132"></td>
                                    <td>Moris</td>
                                    <td>4</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>2</td>
                                </tr>
                                
                                <tr class="ringlon-1">
                                    <td class="semaforo"><img src="https://comunicachihuahua.desarrollosenlanube.net/wp-content/uploads/2020/06/semaforoNaranja.png" alt="" width="20" height="20" class="alignnone size-full wp-image-6132"></td>
                                    <td>Dr. Belisario Dom??nguez</td>
                                    <td>3</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>2</td>
                                </tr>
                                
                                <tr class="ringlon-2">
                                    <td class="semaforo"><img src="https://comunicachihuahua.desarrollosenlanube.net/wp-content/uploads/2020/06/semaforoNaranja.png" alt="" width="20" height="20" class="alignnone size-full wp-image-6132"></td>
                                    <td>Matach??</td>
                                    <td>2</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>1</td>
                                </tr>
                                
                                <tr class="ringlon-1">
                                    <td class="semaforo"><img src="https://comunicachihuahua.desarrollosenlanube.net/wp-content/uploads/2020/06/semaforoNaranja.png" alt="" width="20" height="20" class="alignnone size-full wp-image-6132"></td>
                                    <td>Rosario</td>
                                    <td>3</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>-</td>
                                </tr>
                                
                                <tr class="ringlon-2">
                                    <td class="semaforo"><img src="https://comunicachihuahua.desarrollosenlanube.net/wp-content/uploads/2020/06/semaforoNaranja.png" alt="" width="20" height="20" class="alignnone size-full wp-image-6132"></td>
                                    <td>Maguarichi</td>
                                    <td>1</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>-</td>
                                </tr>
                                
                                <tr class="ringlon-1">
                                    <td class="semaforo"><img src="https://comunicachihuahua.desarrollosenlanube.net/wp-content/uploads/2020/06/semaforoNaranja.png" alt="" width="20" height="20" class="alignnone size-full wp-image-6132"></td>
                                    <td>Uruachi</td>
                                    <td>1</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>-</td>
                                </tr>
                                
                                <tr class="ringlon-2">
                                    <td class="semaforo"></td>
                                    <td>M??xico</td>
                                    <td>1,100,683</td>
                                    <td>407,631</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>105,655 </td>
                                </tr>
                                
                                <tr class="ringlon-1">
                                    <td class="semaforo"></td>
                                    <td>Mundial</td>
                                    <td>61,869,330</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>1,448,896</td>
                                </tr>
                                </tbody></table></div>

        <div id="fechahora">Corte: 14 de Dic. del 2020, 8:00 AM</div>

             <img src="https://comunicachihuahua.desarrollosenlanube.net/wp-content/uploads/2020/03/Fase3.png" class="vc_single_image-img attachment-full" alt="" srcset="https://comunicachihuahua.desarrollosenlanube.net/wp-content/uploads/2020/03/Fase3.png 450w, 
            https://comunicachihuahua.desarrollosenlanube.net/wp-content/uploads/2020/03/Fase3-300x30.png 300w" sizes="(max-width: 450px) 100vw, 450px" data-full-width="450" data-full-height="45" data-pin-no-hover="true">


        <div data-vc-full-width="true" data-vc-full-width-init="true" data-vc-stretch-content="true" class="row vc_row vc_custom_1586230568361 vc_row-no-padding" style="position: relative; left: 0px; box-sizing: border-box; width: 339px;">
            <div class="jeg-vc-wrapper">
                <div class="wpb_column jeg_column vc_column_container vc_col-sm-12 jeg_main_content">
                    <div class="jeg_wrapper wpb_wrapper">
                        <div class="vc_empty_space" style="height: 22px">
                            <span class="vc_empty_space_inner"></span>
                        </div>
                        <div class="wpb_text_column wpb_content_element ">
                            <div class="wpb_wrapper">
                                <p></p>
                                <center><iframe src="https://www.youtube.com/embed/videoseries?list=PL4YJCY6AeSLJJ6r7A-dMyqgyxFDheoenP&amp;showinfo=1" width="100%" height="280" frameborder="0" allowfullscreen="allowfullscreen"></iframe></center>
                                <p></p>

                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <div class="slider-daniel">
            <div class="slider-diapositiva" id="lamina1" style="display: none;">
                <img src="https://comunicachihuahua.desarrollosenlanube.net/wp-content/uploads/2020/03/ll1-1.png">
            </div>
            <div class="slider-diapositiva" id="lamina2" style="">
                <img src="https://comunicachihuahua.desarrollosenlanube.net/wp-content/uploads/2020/03/ll2-1.png">
            </div>
            <div class="slider-diapositiva" id="lamina3" style="display: none;">
                <img src="https://comunicachihuahua.desarrollosenlanube.net/wp-content/uploads/2020/03/ll3-1.png">
            </div>
            <div class="slider-diapositiva" id="lamina4" style="display: none;">
                <img src="https://comunicachihuahua.desarrollosenlanube.net/wp-content/uploads/2020/03/ll4-1.png">
            </div>
        </div>
            <div class="slider-controles">
                <div class="boton" id="btn1" data-slide="1"><br></div>
                <div class="boton boton-activo" id="btn2" data-slide="2"><br></div>
                <div class="boton" id="btn3" data-slide="3"><br></div>
                <div class="boton" id="btn4" data-slide="4"><br></div>
            </div>


        <img width="350" height="515" src="img/v-1002/cuidado.jpeg" class="vc_single_image-img attachment-full" alt="" srcset="img/v-1002/cuidado.jpeg 350w, 
            img/v-1002/cuidado.jpeg 204w" sizes="(max-width: 350px) 100vw, 350px" data-full-width="350" data-full-height="515" data-pin-no-hover="true">

            <img src="img/banner.png" id="btn_plan" style="width: 90%; height: auto; margin-left: 5%; margin-top: 10px;">

            <img src="img/banner2.png" id="btn_videos" style="width: 90%; height: auto; margin-left: 5%; margin-top: 10px;">

            <div class="Noticias-titulo">Noticias</div>
            <hr>
            <div class="noticias-contgenedor">
                              <div class="caja-noticia" data-noticia="0">
                    <h2>Restricciones de emergencia bajaron pico de contagios de 4,807 hasta 1,362 por semana</h2>
                    <img src="https://i0.wp.com/comunicachihuahua.desarrollosenlanube.net/wp-content/uploads/2020/12/restricciones-de-emergencia-bajaron-pico-de-contagios-de-4807-hasta-1362-por-semana_5fd3e286cfadd.jpeg">
                </div>
                <div class="noticia-cuerpo" id="noti0" style="display: none;">
                    <div class="cerrar-noticia"> <i class="fad fa-arrow-circle-left"></i>  Atr??s</div>
                    <img src="https://i0.wp.com/comunicachihuahua.desarrollosenlanube.net/wp-content/uploads/2020/12/restricciones-de-emergencia-bajaron-pico-de-contagios-de-4807-hasta-1362-por-semana_5fd3e286cfadd.jpeg">
                    <h1>Restricciones de emergencia bajaron pico de contagios de 4,807 hasta 1,362 por semana</h1>
                    <div class="content-inner">
                            <div class="noticia_full">
<div class="jeg_share_button share-float jeg_sticky_share clearfix share-monocrhome">
                                                    </div>

                        <div class="content-inner ">
                            <p>El reto es no hacer congregaciones por el D??a de la Virgen ni reuniones navide??as para mantener a la baja los niveles de contagio y fallecimientos; advierte la Secretar??a de Salud que no se debe ver a la vacuna contra el COVID-19 como la soluci??n a la crisisLa subsecretaria de Prevenci??n y Promoci??n de la Salud, Mirna Beltr??n Arzaga, inform?? que gracias a las medidas que ha emprendido el Gobierno del Estado para controlar la pandemia, la estad??stica regres?? al nivel que se registr?? entre la semana 40 a la 41.<br>
Explic?? que en la semana 48 el n??mero de casos disminuy?? a mil 362, luego del pico de 4 mil 807 registrado en octubre.<br>
Igualmente los fallecimientos, de haber registrado un pico de 380 decesos en la semana 45, han disminuido a 224 gracias a las estrategias emprendidas, se??al?? la Dra. Beltr??n.<br>
Al hablar de los resultados ante la pandemia en el programa Chihuahua Adelante No. 85 del gobernador Javier Corral, la funcionaria de salud se??al?? que lo m??s importante son los retos.<br>
Se??al?? al respecto que ???el gran reto que tenemos como ciudadan??a y como Gobierno, es mantener una curva lo m??s controlada posible, como lo tuvimos a lo largo de 27 semanas epidemiol??gicas, es decir, de marzo a septiembre y evitar que se vuelva a presentar algo como en el mes de octubre.<br>
Invit?? a que este 12 de diciembre en que se celebra a la Virgen de Guadalupe la gente por favor no acuda ni haga peregrinaciones o congregaciones, ya que los templos van a estar cerrados.<br>
En cuanto a la Navidad y el A??o Nuevo, pidi?? igualmente evitar las reuniones familiares y las celebraciones, porque ???esos 4 mil 800 casos de la semana con m??s contagios, se pueden convertir en 8 mil o en 12 mil y nos puede llevar a un escenario realmente catastr??fico, peor del que vivimos en el mes de octubre???.<br>
Las recomendaciones de la Secretar??a de Salud para la Navidad son las siguientes: celebrar reuniones navide??as en casa solo con los integrantes del hogar; hacer compras y regalos seguros; hacer donaciones o actividades altruistas, incluso posadas en albergues y asilos con todas las medidas de prevenci??n; reforzar los h??bitos de vida saludable ???Navidad con salud??? ???Navidad en Casa??? y las medidas generales preventivas.<br>
La doctora Beltr??n explic?? durante el programa que la base de informaci??n de la Secretar??a es la vigilancia epidemiol??gica y ??sta indica que el gran reto es este mes de diciembre por lo que representa.<br>
No son solo estad??sticas o n??meros fr??os, ???son personas que enfermaron o fallecieron y son personas que usted y yo conocimos, que usted y yo perdimos a lo largo del camino y que en honor a todo eso, es que como poblaci??n debemos de tomar las medidas preventivas, tener esa responsabilidad y vigilar que el resto de las personas tambi??n utilicen su cubrebocas, se laven las manos, mantengamos la sana distancia, evitemos esas reuniones y la congregaci??n de personas en las cuales se puede generar los contagios???.<br>
Beltr??n Arzaga advirti?? adem??s que se est?? pensando que la una vez que llegue la vacuna todo quedar?? solucionado cuando no ser?? as??.<br>
Se??al?? que en las ??ltimas semanas se aceler?? la informaci??n en torno a las vacunas que pr??cticamente est??n aqu?? a la vuelta de la esquina, sin embargo no son la soluci??n a la pandemia.<br>
???No lo es, eso debemos de grabarnos muy bien, porque hemos estado visualizando, se est?? creando una sensaci??n de seguridad y no se pueden relajar las medidas, no puede dejar de utilizar el cubrebocas, no se puede realizar una reuni??n, una fiesta, porque el riesgo contin??a???, indic??.<br>
Explic?? que si todo sale bien, los efectos de una vacuna se ver??n hasta finales del 2021 o 2022, porque para que el total de la poblaci??n a nivel nacional y estatal est?? vacunado al 100%, ser?? hasta 2022.<br>
Adem??s, agreg??, tampoco se sabe a??n cu??nto va a durar la inmunidad de la vacuna, que recordemos, est??n todav??a en investigaci??n y a??n no tienen resultados al cien por ciento.</p>
                            
	                        
                                                    </div>
</div>
                          </div>
                </div>
                        
                              <div class="caja-noticia" data-noticia="1">
                    <h2>Tiene app Salud Digital 113 mil 831 registros para atenci??n a COVID-19</h2>
                    <img src="https://i1.wp.com/comunicachihuahua.desarrollosenlanube.net/wp-content/uploads/2020/12/tiene-app-salud-digital-113-mil-831-registros-para-atencion-a-covid-19_5fd3d4c631d11.jpeg">
                </div>
                <div class="noticia-cuerpo" id="noti1" style="display: none;">
                    <div class="cerrar-noticia"> <i class="fad fa-arrow-circle-left"></i>  Atr??s</div>
                    <img src="https://i1.wp.com/comunicachihuahua.desarrollosenlanube.net/wp-content/uploads/2020/12/tiene-app-salud-digital-113-mil-831-registros-para-atencion-a-covid-19_5fd3d4c631d11.jpeg">
                    <h1>Tiene app Salud Digital 113 mil 831 registros para atenci??n a COVID-19</h1>
                    <div class="content-inner">
                            <div class="noticia_full">
<div class="jeg_share_button share-float jeg_sticky_share clearfix share-monocrhome">
                                                    </div>

                        <div class="content-inner ">
                            <p>La estrategia permite que desde un dispositivo m??vil, cualquier persona reciba teleconsultas y orientaci??n sobre la sintomatolog??a que presenta, sin tener que movilizarse, se??ala subdirectora Mirna Beltr??n Arzaga, en el programa Chihuahua AdelanteTodo el personal m??dico que est?? detr??s del esquema es experto, afirma Hugo Ren??n Covi??n, coordinador de la Gerencia Amarilla; la aplicaci??n enlaza a las diferentes instituciones cl??nicas<br>
Una de las herramientas m??s efectivas en la estrategia de la Secretar??a de Salud Estatal para contener los contagios de COVID-19 es la aplicaci??n Salud Digital, que ya cuenta con 113 mil 831 registros, inform?? la subsecretaria de Prevenci??n y Promoci??n de la Salud, Mirna Beltr??n Arzaga, en el programa Chihuahua Adelante.<br>
La funcionaria destac?? que a la fecha se ha dado seguimiento a m??s de 15 mil casos sospechosos, de gente que report?? su sintomatolog??a para saber si son o no portadores del Sars-Cov2 y recibir orientaci??n m??dica gratuita, sin tener que movilizarse.<br>
???A lo largo de todos estos meses, Salud Digital ha ido creciendo, se ha ido perfeccionando, ya contamos con un enlace hacia nuestros expedientes electr??nicos, est?? ligada al 9-1-1, podemos brindar una teleconsulta, hacemos el seguimiento de pacientes y brindamos informaci??n???, indic??.<br>
Resalt?? que la app (aplicaci??n) puede ser utilizada por cualquier persona, independientemente de su derechohabiencia m??dica, ya que cuenta con un link para enlazarse con el resto de las instituciones y su respectivo expediente personal, para que la atenci??n quede bien documentada.<br>
El esquema de Salud Digital se divide en cuatro gerencias, verde, amarillo, naranja y rojo, a las que se canaliza a la usuaria y usuario que se registr??, seg??n su riesgo de tener COVID-19, se??al?? la subsecretaria.<br>
Adem??s, el esquema tambi??n brinda orientaci??n sobre el estado mental, situaci??n de violencia y salud materna, destac??.<br>
???De acuerdo a las respuestas que usted da, se clasifica la informaci??n y los diferentes m??dicos, psic??logos y nutri??logos que nos est??n ayudando, le realizan la llamada y determinan la periodicidad en la que se va a estar realizando el seguimiento, y as?? evitamos que las personas est??n moviliz??ndose en los espacios p??blicos???, explic??.<br>
Sin embargo, advirti?? que no significa que el objetivo sea dejar a todas y todos siempre en casa, pues en el momento en que sea identificado un riesgo ante el cual la o el paciente deba acudir a una unidad de salud, se le indicar??.<br>
???Hasta ahora 113 mil 831 usuarias y usuarios registrados en la plataforma, y 94 mil 736 registros dentro de Salud Digital???, expuso.<br>
Dijo que la diferencia entre estos n??meros, obedece a que una misma persona puede registrar a varios miembros de su familia.<br>
Mencion?? que el 81 por ciento de quienes se dieron de alta en la app, no tuvieron COVID-19, aunque si la persona detecta que sus s??ntomas cambiaron puede actualizarlos y el mecanismo se detona nuevamente desde el principio para evaluarlos.<br>
Hugo Ren??n Covi??n, coordinador de los 18 m??dicos que integran la Gerencia Amarilla de Salud Digital, tambi??n particip?? en la emisi??n de Chihuahua Adelante y coment?? que todo el personal que atiende esta emergencia es experto en detectar la sintomatolog??a de esta enfermedad.<br>
???En la gerencia amarilla, en los ??ltimos 15 d??as se registraron aproximadamente 350 personas, que requirieron atenci??n telef??nica, y a todas ellas se les da seguimiento al 100 por ciento???, coment??.<br>
Dijo que el m??dico que llama por primera vez a la o el paciente, es quien dar?? el seguimiento, pero todo el equipo de salud puede participar para que el tratamiento sea integral.<br>
???Al ver las notas del paciente, tal vez yo, como psic??logo, voy a dar seguimiento a alguien que tambi??n la gerencia amarilla est?? viendo, y ah?? me doy cuenta de c??mo han disminuido los s??ntomas, para que mi intervenci??n psicol??gica sea m??s eficiente???, observ??.<br>
Recalc?? que el dinamismo de esta aplicaci??n digital agreg?? un par de preguntas relacionadas con la disposici??n y uso del ox??metro.<br>
???Nos dimos cuenta de que muchos de nuestros pacientes empezaron a sentir un cansancio o una fatiga muy extrema y pensaron que era algo normal, sin embargo, era un reflejo de que su saturaci??n de ox??geno era muy baja???, comparti??.<br>
Una vez que se conoce la cifra que arroja esta herramienta, el personal m??dico marca como ???un poquito alarmante de 94 hacia abajo, pero el paciente puede continuar en su domicilio, siempre y cuando ese saturaci??n no se degrade por debajo de 90, entonces, contar con el ox??metro es muy muy importante???, afirm??.<br>
Salud Digital est?? disponible para cualquier dispositivo m??vil, y se puede descargar de manera gratuita, de las tiendas de aplicaciones de Android y de iOs.<br>
Una vez instalada en el tel??fono celular, se ingresa al apartado Reg??strate y averigua si eres sospechoso de COVID-19, y recibir??s un c??digo de seguridad para escribir tu nombre y datos generales.<br>
La aplicaci??n es segura y toda la informaci??n personal ingresada es confidencial.<br>
Para continuar se invita a la persona a llenar un cuestionario de 12 preguntas sobre la sintomatolog??a, y seg??n la cantidad y tipo de respuestas positivas, se cataloga al paciente con un color, para priorizar la atenci??n.<br>
A los grupos amarillo, naranja y rojo se les dar?? un seguimiento, y se les explica c??mo es el proceso para recibir atenci??n y monitoreo.</p>
                            
	                        
                                                    </div>
</div>
                          </div>
                </div>
                        
                              <div class="caja-noticia" data-noticia="2">
                    <h2>Revisan Brigadas de Salud Estatal vulnerabilidad comunitaria ante COVID casa por casa</h2>
                    <img src="https://i2.wp.com/comunicachihuahua.desarrollosenlanube.net/wp-content/uploads/2020/12/revisan-brigadas-de-salud-estatal-vulnerabilidad-comunitaria-ante-covid-casa-por-casa_5fd3d46a7242e.jpeg">
                </div>
                <div class="noticia-cuerpo" id="noti2" style="display: none;">
                    <div class="cerrar-noticia"> <i class="fad fa-arrow-circle-left"></i>  Atr??s</div>
                    <img src="https://i2.wp.com/comunicachihuahua.desarrollosenlanube.net/wp-content/uploads/2020/12/revisan-brigadas-de-salud-estatal-vulnerabilidad-comunitaria-ante-covid-casa-por-casa_5fd3d46a7242e.jpeg">
                    <h1>Revisan Brigadas de Salud Estatal vulnerabilidad comunitaria ante COVID casa por casa</h1>
                    <div class="content-inner">
                            <div class="noticia_full">
<div class="jeg_share_button share-float jeg_sticky_share clearfix share-monocrhome">
                                                    </div>

                        <div class="content-inner ">
                            <p>Ver??nica Carre??n Falc??n, epidemi??loga coordinadora del equipo en el municipio juarense, explica en Chihuahua Adelante, que la estrategia se basa en acudir a colonias de Chihuahua y Ju??rez donde en los ??ltimos 15 d??as hubo casos y fallecimientos por esta enfermedad, para identificar s??ntomas y comorbilidades que pudieran detonar cadenas de transmisi??n y m??s decesos Las Brigadas de Atenci??n a Pacientes COVID-19, de la Secretar??a de Salud Chihuahua, a diario recorren las diversas colonias de Ciudad Ju??rez y Chihuahua para medir la vulnerabilidad comunitaria y brindar una intervenci??n temprana que evite cadenas de contagio de esta y otras enfermedades.<br>
Ver??nica Carre??n Falc??n, epidemi??loga coordinadora del equipo en el municipio juarense, mediante un enlace virtual al programa Chihuahua Adelante, se??al?? que la estrategia es llegar a cada casa para identificar posibles casos de diversos padecimientos y canalizarlos a unidades de segundo nivel.<br>
Con esto ???explic??- se evita que se compliquen y que ocurran decesos por falta de atenci??n m??dica.<br>
Resalt?? que a la fecha hay 12 brigadas que miden la vulnerabilidad comunitaria en cuesti??n de salud, en Ciudad Ju??rez, y se trabaja para integrar a m??s, por medio de la red de Servicios de Salud de la Secretar??a de Salud Estatal.<br>
En el marco de la pandemia de COVID-19, el objetivo es identificar a las y los ciudadanos con factores de riesgo de infectarse con Sars-Cov2, como puede ser la hipertensi??n arterial, diabetes y asma.<br>
De igual manera, las brigadas eval??an la salud materna: ???a las embarazadas, es muy importante detectarlas de manera oportuna, para prevenir que vayan a tener un embarazo complicado que pudiera ocasionar la muerte tanto de la madre como del beb?????, indic??.<br>
La epidemi??loga dijo que la selecci??n de manzanas a visitar en las colonias, se basa en un sistema de georefernciaci??n que toma en cuenta factores determinantes, como la cantidad de pacientes con COVID, detectados en los ??ltimos 15 d??as.<br>
???Identificamos las colonias que tienen riesgo, ya sea por el n??mero de casos o por el n??mero de defunciones que ha presentado. Y la finalidad de estas acciones es que la poblaci??n no se mueva y tenga una menor movilidad para evitar el n??mero de contagios???, coment??.<br>
Comparti?? que d??a a d??a a las 8 la ma??ana, las brigadas parten de la Jurisdicci??n Sanitaria correspondiente, con el equipo y personal m??dico preparado un d??a anterior.<br>
Destac?? que en general la recepci??n que les ha dado la ciudadan??a ha sido buena, pues se ha mostrado dispuesta a recibir la informaci??n y recomendaciones.<br>
Explic?? que cuando es detectada una persona con sintomatolog??a de COVID-19, se le comunica a una brigada m??dica especializada, integrada por una enfermera y otras personas que acuden a valorar la condici??n del paciente, as?? como a tomar muestras.<br>
La funcionaria recomend?? a la poblaci??n, que en caso de ser necesario, puede llamar al n??mero de atenci??n a emergencias 9-1-1, para ser trasladada a una unidad de segundo nivel.</p>
                            
	                        
                                                    </div>
</div>
                          </div>
                </div>
                        
                              <div class="caja-noticia" data-noticia="3">
                    <h2>Registra Salud 253 nuevos casos y 33 decesos por COVID-19 en el estado</h2>
                    <img src="https://i1.wp.com/comunicachihuahua.desarrollosenlanube.net/wp-content/uploads/2020/12/registra-salud-253-nuevos-casos-y-33-decesos-por-covid-19-en-el-estado_5fd3d0ea3e1c2-scaled.jpeg">
                </div>
                <div class="noticia-cuerpo" id="noti3" style="display: none;">
                    <div class="cerrar-noticia"> <i class="fad fa-arrow-circle-left"></i>  Atr??s</div>
                    <img src="https://i1.wp.com/comunicachihuahua.desarrollosenlanube.net/wp-content/uploads/2020/12/registra-salud-253-nuevos-casos-y-33-decesos-por-covid-19-en-el-estado_5fd3d0ea3e1c2-scaled.jpeg">
                    <h1>Registra Salud 253 nuevos casos y 33 decesos por COVID-19 en el estado</h1>
                    <div class="content-inner">
                            <div class="noticia_full">
<div class="jeg_share_button share-float jeg_sticky_share clearfix share-monocrhome">
                                                    </div>

                        <div class="content-inner ">
                            <p>Llama a la poblaci??n a no bajar la guardia este s??bado 12 de diciembre, d??a que se celebra a la Virgen de Guadalupe; invita a evitar las tradicionales peregrinaciones y celebraciones presencialesLos registros de contagios y defunciones por COVID-19 siguen a la baja en la semana 48, sin embargo a??n representan un riesgo para la poblaci??n, mencion?? el director m??dico de la Secretar??a de Salud en la zona norte, Arturo Valenzuela Zorrilla en la conferencia Informativa #294 y Virtual #254 del Reporte COVID-19.<br>
???Seguimos con n??meros descendentes, por fortuna, a??n no llegamos al margen de seguridad, sin embargo si nos seguimos esforzando pronto estaremos en condiciones de ir abriendo un poco m??s la econom??a???, mencion??.<br>
De esa forma, el total de casos acumulados a la fecha es de 41 mil 730 con 253 nuevos contagios, as?? como 3 mil 900 personas fallecidas, al registrarse 33 decesos m??s, de los cuales, 16 fueron confirmados en Ju??rez, 7 en la ciudad de Chihuahua, 2 en Delicias, 2 en Ahumada, as?? como uno en cada uno de los siguientes municipios: Parral, Cuauht??moc, Nuevo Casas Grandes, Madera, Santa B??rbara y Moris.<br>
El funcionario m??dico llam?? a la poblaci??n a no bajar la guardia este s??bado 12 de diciembre, d??a que se celebra a la Virgen de Guadalupe, por lo que invit?? a la feligres??a cat??lica a evitar celebraciones presenciales como las tradicionales peregrinaciones.<br>
Precis?? que a la fecha van 117 mil 851 inscripciones en la aplicaci??n para celular ???Salud Digital???, que tiene como fin registrar y atender casos de COVID-19 en Chihuahua.<br>
Del total de registros 74 mil 313 recibieron en respuesta Gerencias Blanco/Verde, otros 3 mil 423 recibieron atenci??n catalogada como COVID-19 (Amarillo) y 6 mil 207 atenci??n catalogada como COVID-19 (Rojo/Naranja); en cuanto a Monitor Covid, se han sumado 4 mil 150 personas a la lucha de evitar contagios.<br>
Se inform?? tambi??n que se tienen 22 mil 724 (+398) recuperados, 21 mil 575 (+163) descartados y 2,864 (-82) sospechosos.<br>
Mencion?? que los contagios por municipio son los siguientes: Ahumada 77, Aldama 97, Allende 70, Ascensi??n 63, Aquiles Serd??n 151, Bach??niva 14, Batopilas 6, Bocoyna 268, Balleza 9, Buenaventura 34, Camargo 285, Carich?? 8, Casas Grandes 24, Chihuahua 9,523, Ch??nipas 115, Coronado 5, Coyame del Sotol 8, Cuauht??moc 1,312, Cusihuiriachi 13, Delicias 1,628, Dr. Belisario Dom??nguez 3, Galeana 7, G??mez Far??as 68, Guachochi 233, Gran Morelos 8, Guadalupe 14, Guadalupe y Calvo 28, Guazapares 64 y Guerrero 60.<br>
Parral 1,505, Ignacio Zaragoza 12, Janos 18, Jim??nez 187, Ju??rez 23,586, Julimes 9, L??pez 8, Madera 35, Manuel Benavides 25, Matach?? 2, Meoqui 219, Moris 4, Namiquipa 67, Nonoava 16, Nuevo Casas Grandes 630, Ocampo 15, Ojinaga 740, Praxedis G. Guerrero 11, Riva Palacio 6, Rosales 59, Rosario 3, San Francisco del Oro 23, Santa B??rbara 61, Satev?? 5, Saucillo 169, Tem??sachic 9, Urique 36, Valle de Zaragoza 11, San Francisco de Conchos 11, Santa Isabel 11, La Cruz 19, San Francisco de Borja 5, Maguarichi 1, El Tule 4, Matamoros 14 y Uruachi 1.<br>
La informaci??n muestra que el 51% son del sexo masculino (21,439 casos) y 49% femenino (20,291 casos).<br>
En cuanto a decesos por municipio inform?? que van 2,291 en Ju??rez, 771 Chihuahua, 185 Delicias, 141 Parral, 121 Cuauht??moc, 55 Nuevo Casas Grandes, 41 Meoqui, 39 Camargo, 32 Saucillo, 19 Guerrero, 20 Jim??nez, 14 Guachochi, 12 Ascensi??n, 11 Rosales, 9 Ahumada, 6 Bocoyna, 8 Ojinaga, 5 Carich??, 6 Namiquipa, 5 Tem??sachic, 7 Aquiles Serd??n, 7 Buenaventura, 8 Madera, 6 San Francisco del Oro, 7 Aldama, 5 Casas Grandes, 4 Galeana, 4 Ocampo, 4 Urique, 4 G??mez Far??as, 3 Riva Palacio, 3 Janos, 4 Julimes, 3 Coronado y 3 Guadalupe D. B.<br>
Adem??s, 3 en Ignacio Zaragoza, 3 Cusihuiriachi, 2 Dr. Belisario Dom??nguez, 3 Coyame del Sotol, 2 Moris, 1 Allende, 2 Balleza, 1 Matach??, 1 Bach??niva, 1 Guazapares, 2 Valle de Zaragoza, 1 Santa Isabel, 3 L??pez, 3 San Francisco de Conchos, 4 Santa B??rbara, 2 Guadalupe y Calvo, 1 Gran Morelos, 1 Nonoava y 1 El Tule.<br>
Edades de pacientes fallecidos: 6 casos menores a un a??o; 2 de 1 a 4; 2 de 5 a 9; 3 de 10 a 14; 2 de 15 a 19; 16 de 20 a 24; 33 de 25 a 29; 68 de 30 a 34; 87de 35 a 39; 192 de 40 a 44; 290 de 45 a 49; 386 de 50 a 54; 474 de 55 a 59; 543 de 60 a 64; 479 de 65 a 69; 471 de 70 a 74; 388 de 75 a 79; 272 de 80 a 84; 121 de 85 a 89; 46 de 90 a 94; 16 de 95 a 99 y 3 de 100 a 104 a??os de edad.<br>
Porcentajes de comorbilidad en fallecimientos: 34% hipertensi??n, 25% diabetes, 16% obesidad, 6% tabaquismo, 6% otra condici??n, 4% enfermedad cardiaca, 4% insuficiencia renal, 2% EPOC, 2% inmunosupresi??n, 1% asma, 0.3% VIH/Sida. La proporci??n es 39% mujeres y 61% hombres.<br>
En este momento el estado tiene 405 pacientes hospitalizados: 56% en el IMSS, 24% en el Sector Salud, 6% en el Issste, 13% en Sedena, 1% en IMSS Bienestar. De esos, 96 est??n intubados, 52% en el IMSS, 39% en SSA, 7% en el Issste y 2% en Sedena. Con reporte de 29 hospitales.<br>
Muestras de diagn??stico: Laboratorio Estatal 81, acumuladas 31,774; otros laboratorios 400, acumuladas 100,490; total de muestras 481, acumuladas 132,234.<br>
El reporte indica que en El Paso, Texas van 91,468 casos confirmados (+275 nuevos +43 casos con retraso), 1,121 decesos (+44) y 52,188 recuperados (+675).</p>
                            
	                        
                                                    </div>
</div>
                          </div>
                </div>
                        
                              <div class="caja-noticia" data-noticia="4">
                    <h2>Posicionamiento de la SEyD sobre los Centros Comunitarios de Aprendizaje</h2>
                    <img src="https://i2.wp.com/comunicachihuahua.desarrollosenlanube.net/wp-content/uploads/2020/12/posicionamiento-de-la-seyd-sobre-los-centros-comunitarios-de-aprendizaje_5fd3bf5256bf7.jpeg">
                </div>
                <div class="noticia-cuerpo" id="noti4" style="display: none;">
                    <div class="cerrar-noticia"> <i class="fad fa-arrow-circle-left"></i>  Atr??s</div>
                    <img src="https://i2.wp.com/comunicachihuahua.desarrollosenlanube.net/wp-content/uploads/2020/12/posicionamiento-de-la-seyd-sobre-los-centros-comunitarios-de-aprendizaje_5fd3bf5256bf7.jpeg">
                    <h1>Posicionamiento de la SEyD sobre los Centros Comunitarios de Aprendizaje</h1>
                    <div class="content-inner">
                            <div class="noticia_full">
<div class="jeg_share_button share-float jeg_sticky_share clearfix share-monocrhome">
                                                    </div>

                        <div class="content-inner ">
                            <p>En ese tenor, Chihuahua reinicia la planeaci??n de la estrategia local denominada ???Centros de Asesor??a y Acompa??amiento???, para cuando las diversas regiones de la entidad se encuentren en sem??foro epidemiol??gico color amarillo; pero ya sin considerarlo como un pilotaje, sino como una estrategia general y nacionalDurante la LI Sesi??n del Consejo Nacional de Autoridades Educativas, CONAEDU, el Secretario de Educaci??n P??blica del Gobierno de M??xico, Esteban Moctezuma Barrag??n, reiter?? el  de la estrategia de los Centros Comunitarios de Aprendizaje como una estrategia previa a un eventual re de clases presenciales, en la que se tomar??n en cuenta los siguientes factores:<br>
 ??	Sem??foro de Riesgo Epidemiol??gico en color amarillo, mismo que permite una mayor movilidad social con medidas de prevenci??n. En este nivel, muchas actividades econ??micas, sociales y culturales son aperturadas con porcentajes de asistencia, lo que hace previsible el  de un modelo especial para las escuelas ubicadas en dichas regiones. ??	Actividad de car??cter voluntaria de maestras y maestros, lo que permite considerar aquellas escuelas cuyos docentes est??n en circunstancias de salud que les permita participar sin riesgos. ??	Horarios restringidos, considerando que la actividad principal de estos Centros ser??a el acompa??amiento, asesor??a y reforzamiento acad??mico de los alumnos que as?? lo requieran, al igual que la atenci??n a las madres y padres de familia. ??	Acciones previas de limpieza e higienizaci??n de los centros escolares. ??	Capacidad limitada de atenci??n diaria a alumnas, alumnos y en su caso, madres y padres de familia o tutores, con la posibilidad de generar estrategias de atenci??n por d??as espec??ficos a alumnos con requerimientos de atenci??n especiales.<br>
En ese sentido, los Centros Comunitarios de Aprendizaje no implican la apertura de todas las escuelas ni mucho menos un re de actividades presenciales acad??micas regulares en sem??foro amarillo. Solamente responden a una realidad en la que la movilidad es mucho m??s amplia en todas las personas, incluidos quienes inciden en el hecho educativo.<br>
Es importante en el caso de Chihuahua, se??alar lo siguiente:<br>
Desde el pasado d??a 14 de octubre, en comparecencia ante el H. Congreso del Estado, la Secretar??a de Educaci??n y Deporte (SEyD) inform?? de una estrategia local para iniciar un plan piloto en diversas escuelas de la entidad, p??blicas y privadas, rurales, urbanas e ind??genas, con el prop??sito de iniciar en ellas lo que entonces se denomin?? ???Centros de Asesor??a y Acompa??amiento???, bajo las mismas premisas generales que hoy avala la SEP y en nuestro caso, tomando en consideraci??n dos acciones:<br>
 ??	Que el programa ???Aprende en Casa II??? no estaba teniendo la proyecci??n y la efectividad prevista, toda vez que en el territorio estatal la cobertura de la se??al de televisi??n abierta alcanza un 60%, lo que implica la necesidad de desarrollar otras acciones paralelas para el reforzamiento acad??mico. ??	Que el modelo nacional no es aplicable en sectores espec??ficos de la comunidad chihuahuense como lo son las escuelas ind??genas y menonitas, tanto por condicionantes socioculturales como por razones de idioma. ??	Que en la primera encuesta aplicada a docentes de Educaci??n B??sica con cierre al 13 de octubre de 2020, un 40% de las maestras y los maestros afirm?? estar realizando actividades de presencialidad con sus alumnos con el fin de apoyarlos en el proceso educativo y reforzar los contenidos acad??micos. Estas acciones, de acuerdo a lo indicado en la encuesta, derivan en el acercamiento de las y los docentes con sus alumnos en espacios no escolares, toda vez que ??stos permanecen cerrados a cualquier actividad desde el mes de marzo del presente a??o. ??	Que de acuerdo a los par??metros de las autoridades sanitarias, el sem??foro amarillo implica una mayor movilizaci??n social y permite la apertura de actividades presenciales en todos los ??rdenes y niveles, aplicando una serie de medidas preventivas. En esa etapa, todas las actividades aumentan sus porcentajes de atenci??n y la movilidad es m??s generalizada, lo que de suyo permite la apertura de los edificios escolares para brindar cierto tipo de servicios educativos como las asesor??as y el acompa??amiento en un esquema de atenci??n presencial, escalonado y limitado, tanto a alumnos como a madres y padres de familia, en su caso.<br>
La regresi??n en el sem??foro epidemiol??gico impidi?? la concreci??n de este Plan Piloto de la SEyD, que en un primer momento consideraba hasta a 30 escuelas de educaci??n b??sica en todo el territorio estatal. Sin embargo, desde el mes de noviembre pasado, la autoridad educativa nacional expuso la necesidad de iniciar con un modelo de transici??n a la normalizaci??n de las actividades educativas, lo que finalmente fue informado el d??a de ayer bajo el mismo esquema y condiciones como en su tiempo se plante?? para el Estado de Chihuahua.<br>
En ese tenor, la Secretar??a de Educaci??n y Deporte informa que reinicia la planeaci??n de esta estrategia para cuando las diversas regiones de la entidad se encuentren en sem??foro epidemiol??gico color amarillo, pero ya sin considerarlo como un pilotaje, sino como una estrategia general y nacional que nos permita abordar de manera m??s directa el proceso de ense??anza aprendizaje bajo los criterios sanitarios imperantes y con las consideraciones del Sector Salud. En ello, se dar?? prioridad a las regiones de mayor riesgo y vulnerabilidad.</p>
                            
	                        
                                                    </div>
</div>
                          </div>
                </div>
                        
                              <div class="caja-noticia" data-noticia="5">
                    <h2>Explica Salud estrategia desplegada para atender la pandemia por COVID-19 en Chihuahua</h2>
                    <img src="https://i1.wp.com/comunicachihuahua.desarrollosenlanube.net/wp-content/uploads/2020/12/explica-salud-estrategia-desplegada-para-atender-la-pandemia-por-covid-19-en-chihuahua_5fd3b64256f41.jpeg">
                </div>
                <div class="noticia-cuerpo" id="noti5" style="display: none;">
                    <div class="cerrar-noticia"> <i class="fad fa-arrow-circle-left"></i>  Atr??s</div>
                    <img src="https://i1.wp.com/comunicachihuahua.desarrollosenlanube.net/wp-content/uploads/2020/12/explica-salud-estrategia-desplegada-para-atender-la-pandemia-por-covid-19-en-chihuahua_5fd3b64256f41.jpeg">
                    <h1>Explica Salud estrategia desplegada para atender la pandemia por COVID-19 en Chihuahua</h1>
                    <div class="content-inner">
                            <div class="noticia_full">
<div class="jeg_share_button share-float jeg_sticky_share clearfix share-monocrhome">
                                                    </div>

                        <div class="content-inner ">
                            <p>La premisa ha sido salvar el mayor n??mero de vidas y cortar la red de contagios; se impulsaron 13 pol??ticas p??blicas, plataformas digitales, capacitaciones y los 10 pasos de la salud para la prevenci??n de la enfermedadBajo la premisa de salvar el mayor n??mero de vidas posibles con acciones oportunas de diagn??stico, aislamiento, seguimiento y atenci??n de casos, as?? como mantener los niveles de contagio COVID-19 en zona segura para la ocupaci??n hospitalaria y romper las cadenas de riesgo, la Secretar??a de Salud del Gobierno del Estado despleg?? una amplia estrategia para contener la pandemia en Chihuahua.<br>
En ella, la corresponsabilidad sociedad y Gobierno es fundamental para mitigar los efectos tanto en la salud como en la econom??a, expres?? la subsecretaria de Prevenci??n y Promoci??n de la Salud. Mirna Beltr??n Arzaga, en el programa Chihuahua Adelante.<br>
Al explicar en qu?? consisten las acciones desplegadas desde que se detect?? la enfermedad y posteriormente cuando se decret?? la pandemia, la funcionaria a cargo de la estrategia indic?? c??mo se ha llegado a algunos l??mites y c??mo se ha superado para seguir brindando la atenci??n adecuada en hospitales y de manera preventiva.<br>
Los objetivos son muy puntuales y el principal es salvar vidas, eso es indiscutible lo que ha llevado a crear diferentes pol??ticas p??blicas que son las que ayudan a un control de esta pandemia y ???algo muy importante es crear ese v??nculo y esa corresponsabilidad entre gobiernos y poblaci??n???, expres??.<br>
Explic?? que desde enero que se conoci?? la existencia del nuevo coronavirus, empezaron a reunirse los diferentes grupos al interior de la Secretar??a de Salud para ir analizando y creando la estrategia, donde las primeras acciones son de promoci??n, prevenci??n, vigilancia epidemiol??gica y la atenci??n m??dica, de diagn??stico y aislamiento.<br>
Estas son acciones esenciales para evitar que las personas lleguen a los hospitales y en las que en el centro siempre debe estar la comunidad, es decir, ???las personas son nuestro eje fundamental para llevar a cabo las acciones, los planes y la orientaci??n adecuada???.<br>
Est?? el primer contacto con el sistema de salud a trav??s del 9-1-1 (911) y la plataforma Salud Digital, donde se hace la identificaci??n de casos sospechosos y seguimiento por medio de video llamadas o tele consultas de casos positivos.<br>
Las acciones de promoci??n de la salud diariamente en las conferencias de prensa por la ma??ana, donde se informa c??mo va evolucionando la pandemia y las acciones necesarias para que la gente tome las mejores decisiones preventivas.<br>
Luego est?? la atenci??n primaria, que es cuando las personas llegan a una unidad de primer nivel para ser diagnosticados e interrogados mediante el estudio epidemiol??gico que se realiza para hacer el rastreo de sus contactos m??s cercanos e iniciar la atenci??n m??dica.<br>
Posteriormente se trabaja en la atenci??n temprana del segundo nivel que es en los hospitales para evitar que la gente llegue con alg??n grado de complicaci??n y pueda desencadenar en una defunci??n.<br>
Otra parte de la estrategia la constituye la Red Chihuahuense de Municipios por la Salud, la cual y tiene varios a??os pero ahora ha sido importante tanto en la prevenci??n como en la atenci??n de casos, ya que son las autoridades municipales el primer contacto con la poblaci??n quienes m??s conocen de la din??mica, del entorno y de las enfermedades.<br>
Son ellos, se??al?? la Dra. Beltr??n, los encargados de minimizar la vulnerabilidad que existe por otro tipo de determinantes sociales de la salud como son el acceso al empleo, a los servicios b??sicos de agua, drenaje, educaci??n y todo esto, en conjunto con las herramientas que les brindamos de c??mo cuidar a su poblaci??n.<br>
De igual manera, las jurisdicciones sanitarias se re??nen con las y los presidentes municipales y sus equipos, para analizar por medio de los diagn??sticos, la problem??tica de salud que se est?? presentando en cada uno y ah?? se toman las decisiones y las acciones necesarias.<br>
Al respecto, Beltr??n Arzaga indic?? que en los pr??ximos d??as, los 67 alcaldes presentar??n un informe de todas las acciones que han realizado ante la pandemia, los resultados y el impacto que se ha tenido en los municipios.<br>
Inform?? que se han impulsado 13 pol??ticas p??blicas que est??n instaladas dentro de los diferentes acuerdos emitidos a lo largo de la pandemia y que se constituyen como un instructivo para ir creando las actividades y las acciones preventivas y activas.<br>
Dentro de esas acciones destac?? el v??nculo con el Tecnol??gico de Monterrey y con la Universidad Aut??noma de Chihuahua, quienes a trav??s de sus investigadores han apoyado para la generaci??n de diferentes herramientas que permiten tomar las mejores decisiones, gracias a la georreferenciaci??n, plataforma que sirve para identificar puntos focales y locales de concentraci??n de casos y el emprendimiento de acciones.<br>
Se han adherido m??s de m??s de 4 mil Monitores COVID y se hace la invitaci??n para que m??s gente se integre a esta gran estrategia de corresponsabilidad para evitar los contagios en los centros de trabajo o haciendo una compra.<br>
Se ha intervenido en m??s de 11 mil entornos a trav??s de diferentes capacitaciones virtuales: m??s de 10,000 trabajadores de la salud y m??s de 11 mil empleadas y empleados de las diferentes dependencias de gobierno y del sector privado.<br>
M??s de 2 mil protocolos han sido revisados y se siguen haciendo porque hay empresas que siguen actualiz??ndose e incluso empresas que todav??a no aperturan ya est??n enviando sus protocolos para estar listos en el momento en el que puedan reabrir.<br>
Los programas b??sicos que son la vacunaci??n y prevenci??n de enfermedades cr??nico degenerativas; son 33 programas preventivos que maneja la Secretar??a de Salud a trav??s de sus 11 jurisdicciones sanitarias.<br>
Adem??s se cuenta con los 10 pasos de la Brigada de Promoci??n de la Salud, dirigida a la poblaci??n: 1. Evaluar la vulnerabilidad comunitaria; 2.Identificar personas en riesgo; 3. Reducir el riesgo de complicarse y morir por COVID-19; 4. Detectar tempranamente a personas enfermas; 5. Otorgar seguimiento estrecho; 6. Brindar atenci??n integral de la salud; 7. Realizar referencias oportunas para la atenci??n; 8. Detectar, estudiar y controlar brotes comunitarios; 9. Dar soporte social solidario y 10. Continuar la atenci??n general en salud.<br>
Otra de las acciones destacadas son las Brigadas de Promoci??n de la Salud que contaron en principio con el apoyo del Salud federal pero que fue retirado por la contingencia por las lluvias en Tabasco. Con esta acci??n se ha llegado al menos a 24 mil habitantes de los diferentes municipios del estado.<br>
Se anexan las gr??ficas con los detalles que apoyan la estrategia de la Secretar??a de Salud del Gobierno del Estado.</p>
                            
	                        
                                                    </div>
</div>
                          </div>
                </div>
                        </div>
            <div class="contadores">
                <div class="Noticias-titulo">Contadores Globales</div>

                <div id="contadores_globales"><div class="cuadro-conteo">
                    <div class="conteo-titulo">
                        <i class="fad fa-users"></i> Usuarios
                    </div>
                    <div class="conteo-conteo">118,946</div>
                </div><div class="cuadro-conteo">
                    <div class="conteo-titulo">
                        <i class="fad fa-mind-share"></i> Salud mental
                    </div>
                    <div class="conteo-conteo">8,419</div>
                </div><div class="cuadro-conteo">
                    <div class="conteo-titulo">
                        <i class="fad fa-stethoscope"></i> Hipertensi??n
                    </div>
                    <div class="conteo-conteo">8,538</div>
                </div><div class="cuadro-conteo">
                    <div class="conteo-titulo">
                        <i class="fad fa-tag"></i> Obesidad
                    </div>
                    <div class="conteo-conteo">6,199</div>
                </div><div class="cuadro-conteo">
                    <div class="conteo-titulo">
                        <i class="fad fa-tag"></i> Diabetes
                    </div>
                    <div class="conteo-conteo">4,897</div>
                </div><div class="cuadro-conteo">
                    <div class="conteo-titulo">
                        <i class="fad fa-head-side-cough"></i> Violencia
                    </div>
                    <div class="conteo-conteo">983</div>
                </div><div class="cuadro-conteo">
                    <div class="conteo-titulo">
                        <i class="fad fa-tag"></i> Embarazos
                    </div>
                    <div class="conteo-conteo">257</div>
                </div><div class="cuadro-conteo">
                    <div class="conteo-titulo">
                        <i class="fad fa-map-pin"></i> Municipios
                    </div>
                    <div class="conteo-conteo">67</div>
                </div></div>

                <br style="clear:both;">
            </div>

            <div class="contadores-empresas">
                <div class="Noticias-titulo">Conteos Empresas</div>

                <div id="contadores_empresas"><div class="cuadro-conteo">
                    <div class="conteo-titulo">
                        Empresas
                    </div>
                    <div class="conteo-conteo">642</div>
                </div><div class="cuadro-conteo">
                    <div class="conteo-titulo">
                        Empleados
                    </div>
                    <div class="conteo-conteo">88,601</div>
                </div><div class="cuadro-conteo">
                    <div class="conteo-titulo">
                        Municipios
                    </div>
                    <div class="conteo-conteo">18</div>
                </div><div class="cuadro-conteo">
                    <div class="conteo-titulo">
                        Formulario
                    </div>
                    <div class="conteo-conteo">39,809</div>
                </div></div>

                <br style="clear:both;">
            </div>
       </div>
    </span>



    </div>
    <div id="mens_permiso" class="hide">
        <div id="seg_pagina1">
        <h1>Permiso para compartir Informacion</h1>
        <div class="texto-alerta">
          Segun nuestra informacion, usted a sido diagnosticado con <b>SARS COVID-19.</b>
            <br>
            ??Desearia compartir sus datos de movilidad con los demas usuarios para asi poder identificar posibles nuevos casos?
            <br>
            Los datos proporcionados seran totalmente anonimos y no se compartiran con ninguna persona externa.
            <br>
            Gracias por su atencion y que se mejore pronto.
    </div>
           <div class="radio-btn" id="btn_seguimiento_si">
              <b>Acepto</b>
            <div class="icono" style="background-color: #176eb9">
       <i class="far fa-check"></i>
            </div>
        </div>

        <div class="radio-btn" id="btn_seguimiento_no">
              <b>Rechazo</b>
            <div class="icono" style="background-color: #176eb9">
       <i class="far fa-times"></i>
            </div>
        </div>
            </div>
        <div id="seg_pagina2" class="hide">
            <h1 id="seg_men"></h1>
             <div id="btn-seg-aceptar" class="btn">Aceptar</div>
        </div>
    </div>
    <div class="float-btn-right hide" id="btn_alerta"><i class="fal fa-exclamation-triangle"></i> Atencion 
            <i class="fal fa-exclamation-triangle"></i> </div>
    <div id="vercion_test" class="hide">Ejecuta funcion. | Ajax sucess | permiso activado | ANDROID undefined | No es Celular</div>
    <div id="vercion_test2" class="hide"></div>
    <div id="espacio-footer">
        <br>
    </div>
    <div class="footer-bar">
        <p><i class="far fa-copyright"></i>Servicios de Salud de Chihuahua 2020 </p>
    </div>
    <div class="hide" id="hd_formulario">373</div>
    <div class="hide" id="hd_raiz">/</div>


</div><div class="ui-loader ui-corner-all ui-loader-default ui-body-a"><span class="ui-loader-icon ui-icon-loading"></span><h1 class="ui-loader-header">loading</h1></div></body></html>"""
soup = BeautifulSoup(html, "html.parser")
# print(soup.prettify())
table = soup.select_one('div.contenedor-general')

header = [[a.getText(strip=True,separator=' ')][0].split() for a in table.find_all('tr', {'class': 'header-table'})]
#
# print(header[0])
# print(len(header[0])) # 7
#
# for t in soup.find_all('tr', {'class': 'ringlon-1'}):
#     print(t)
# for t in soup.find_all('tr', {'class': 'ringlon-1'}):
#     print(t.text)
text1 = [t.text.strip().split() for t in soup.find_all('tr', {'class': 'ringlon-1'})]
text2 = [t.text.strip().split() for t in soup.find_all('tr', {'class': 'ringlon-2'})]

flatten_text1 = [x for sub in text1 for x in sub]
# print(flatten_text1)
flatten_text2 = [y for sub in text2 for y in sub]
# print(flatten_text2)

with open('outz.csv', 'w') as f:
    wr = csv.writer(f, delimiter=',')
    wr.writerow(header[0][1:])
    for row in text1:
        wr.writerow(row)
    for row in text2:
        wr.writerow(row)




