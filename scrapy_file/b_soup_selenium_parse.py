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
                        var datos = CreaArreglo(resp, "°", "¬");
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
                    <div class="cerrar-noticia"> <i class="fad fa-arrow-circle-left"></i>  Atrás</div>
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
        <p><span id="tienda-mensaje">Estás usando una versión antigua de la aplicación, por favor descarga la última versión desde la </span> <span id="tienda"></span></p>
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
                Regístrate y averigua si eres sospechoso de COVID-19
    </div>


         </span>
    <span class="pc-columna-left">
        <div id="contenador">
        <div class="platilla-Titulo">Situación Actual</div>
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
                                    <td>Juárez</td>
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
                                    <td>Cuauhtémoc</td>
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
                                    <td>Aquiles Serdán</td>
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
                                    <td>Gómez Farías</td>
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
                                    <td>Ascensión</td>
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
                                    <td>Santa Bárbara</td>
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
                                    <td>Dr. Belisario Domínguez</td>
                                    <td>3</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>-</td>
                                    <td>2</td>
                                </tr>
                                
                                <tr class="ringlon-2">
                                    <td class="semaforo"><img src="https://comunicachihuahua.desarrollosenlanube.net/wp-content/uploads/2020/06/semaforoNaranja.png" alt="" width="20" height="20" class="alignnone size-full wp-image-6132"></td>
                                    <td>Matachí</td>
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
                                    <td>Mèxico</td>
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
                    <div class="cerrar-noticia"> <i class="fad fa-arrow-circle-left"></i>  Atrás</div>
                    <img src="https://i0.wp.com/comunicachihuahua.desarrollosenlanube.net/wp-content/uploads/2020/12/restricciones-de-emergencia-bajaron-pico-de-contagios-de-4807-hasta-1362-por-semana_5fd3e286cfadd.jpeg">
                    <h1>Restricciones de emergencia bajaron pico de contagios de 4,807 hasta 1,362 por semana</h1>
                    <div class="content-inner">
                            <div class="noticia_full">
<div class="jeg_share_button share-float jeg_sticky_share clearfix share-monocrhome">
                                                    </div>

                        <div class="content-inner ">
                            <p>El reto es no hacer congregaciones por el Día de la Virgen ni reuniones navideñas para mantener a la baja los niveles de contagio y fallecimientos; advierte la Secretaría de Salud que no se debe ver a la vacuna contra el COVID-19 como la solución a la crisisLa subsecretaria de Prevención y Promoción de la Salud, Mirna Beltrán Arzaga, informó que gracias a las medidas que ha emprendido el Gobierno del Estado para controlar la pandemia, la estadística regresó al nivel que se registró entre la semana 40 a la 41.<br>
Explicó que en la semana 48 el número de casos disminuyó a mil 362, luego del pico de 4 mil 807 registrado en octubre.<br>
Igualmente los fallecimientos, de haber registrado un pico de 380 decesos en la semana 45, han disminuido a 224 gracias a las estrategias emprendidas, señaló la Dra. Beltrán.<br>
Al hablar de los resultados ante la pandemia en el programa Chihuahua Adelante No. 85 del gobernador Javier Corral, la funcionaria de salud señaló que lo más importante son los retos.<br>
Señaló al respecto que “el gran reto que tenemos como ciudadanía y como Gobierno, es mantener una curva lo más controlada posible, como lo tuvimos a lo largo de 27 semanas epidemiológicas, es decir, de marzo a septiembre y evitar que se vuelva a presentar algo como en el mes de octubre.<br>
Invitó a que este 12 de diciembre en que se celebra a la Virgen de Guadalupe la gente por favor no acuda ni haga peregrinaciones o congregaciones, ya que los templos van a estar cerrados.<br>
En cuanto a la Navidad y el Año Nuevo, pidió igualmente evitar las reuniones familiares y las celebraciones, porque “esos 4 mil 800 casos de la semana con más contagios, se pueden convertir en 8 mil o en 12 mil y nos puede llevar a un escenario realmente catastrófico, peor del que vivimos en el mes de octubre”.<br>
Las recomendaciones de la Secretaría de Salud para la Navidad son las siguientes: celebrar reuniones navideñas en casa solo con los integrantes del hogar; hacer compras y regalos seguros; hacer donaciones o actividades altruistas, incluso posadas en albergues y asilos con todas las medidas de prevención; reforzar los hábitos de vida saludable “Navidad con salud” “Navidad en Casa” y las medidas generales preventivas.<br>
La doctora Beltrán explicó durante el programa que la base de información de la Secretaría es la vigilancia epidemiológica y ésta indica que el gran reto es este mes de diciembre por lo que representa.<br>
No son solo estadísticas o números fríos, “son personas que enfermaron o fallecieron y son personas que usted y yo conocimos, que usted y yo perdimos a lo largo del camino y que en honor a todo eso, es que como población debemos de tomar las medidas preventivas, tener esa responsabilidad y vigilar que el resto de las personas también utilicen su cubrebocas, se laven las manos, mantengamos la sana distancia, evitemos esas reuniones y la congregación de personas en las cuales se puede generar los contagios”.<br>
Beltrán Arzaga advirtió además que se está pensando que la una vez que llegue la vacuna todo quedará solucionado cuando no será así.<br>
Señaló que en las últimas semanas se aceleró la información en torno a las vacunas que prácticamente están aquí a la vuelta de la esquina, sin embargo no son la solución a la pandemia.<br>
“No lo es, eso debemos de grabarnos muy bien, porque hemos estado visualizando, se está creando una sensación de seguridad y no se pueden relajar las medidas, no puede dejar de utilizar el cubrebocas, no se puede realizar una reunión, una fiesta, porque el riesgo continúa”, indicó.<br>
Explicó que si todo sale bien, los efectos de una vacuna se verán hasta finales del 2021 o 2022, porque para que el total de la población a nivel nacional y estatal esté vacunado al 100%, será hasta 2022.<br>
Además, agregó, tampoco se sabe aún cuánto va a durar la inmunidad de la vacuna, que recordemos, están todavía en investigación y aún no tienen resultados al cien por ciento.</p>
                            
	                        
                                                    </div>
</div>
                          </div>
                </div>
                        
                              <div class="caja-noticia" data-noticia="1">
                    <h2>Tiene app Salud Digital 113 mil 831 registros para atención a COVID-19</h2>
                    <img src="https://i1.wp.com/comunicachihuahua.desarrollosenlanube.net/wp-content/uploads/2020/12/tiene-app-salud-digital-113-mil-831-registros-para-atencion-a-covid-19_5fd3d4c631d11.jpeg">
                </div>
                <div class="noticia-cuerpo" id="noti1" style="display: none;">
                    <div class="cerrar-noticia"> <i class="fad fa-arrow-circle-left"></i>  Atrás</div>
                    <img src="https://i1.wp.com/comunicachihuahua.desarrollosenlanube.net/wp-content/uploads/2020/12/tiene-app-salud-digital-113-mil-831-registros-para-atencion-a-covid-19_5fd3d4c631d11.jpeg">
                    <h1>Tiene app Salud Digital 113 mil 831 registros para atención a COVID-19</h1>
                    <div class="content-inner">
                            <div class="noticia_full">
<div class="jeg_share_button share-float jeg_sticky_share clearfix share-monocrhome">
                                                    </div>

                        <div class="content-inner ">
                            <p>La estrategia permite que desde un dispositivo móvil, cualquier persona reciba teleconsultas y orientación sobre la sintomatología que presenta, sin tener que movilizarse, señala subdirectora Mirna Beltrán Arzaga, en el programa Chihuahua AdelanteTodo el personal médico que está detrás del esquema es experto, afirma Hugo Renán Covián, coordinador de la Gerencia Amarilla; la aplicación enlaza a las diferentes instituciones clínicas<br>
Una de las herramientas más efectivas en la estrategia de la Secretaría de Salud Estatal para contener los contagios de COVID-19 es la aplicación Salud Digital, que ya cuenta con 113 mil 831 registros, informó la subsecretaria de Prevención y Promoción de la Salud, Mirna Beltrán Arzaga, en el programa Chihuahua Adelante.<br>
La funcionaria destacó que a la fecha se ha dado seguimiento a más de 15 mil casos sospechosos, de gente que reportó su sintomatología para saber si son o no portadores del Sars-Cov2 y recibir orientación médica gratuita, sin tener que movilizarse.<br>
“A lo largo de todos estos meses, Salud Digital ha ido creciendo, se ha ido perfeccionando, ya contamos con un enlace hacia nuestros expedientes electrónicos, está ligada al 9-1-1, podemos brindar una teleconsulta, hacemos el seguimiento de pacientes y brindamos información”, indicó.<br>
Resaltó que la app (aplicación) puede ser utilizada por cualquier persona, independientemente de su derechohabiencia médica, ya que cuenta con un link para enlazarse con el resto de las instituciones y su respectivo expediente personal, para que la atención quede bien documentada.<br>
El esquema de Salud Digital se divide en cuatro gerencias, verde, amarillo, naranja y rojo, a las que se canaliza a la usuaria y usuario que se registró, según su riesgo de tener COVID-19, señaló la subsecretaria.<br>
Además, el esquema también brinda orientación sobre el estado mental, situación de violencia y salud materna, destacó.<br>
“De acuerdo a las respuestas que usted da, se clasifica la información y los diferentes médicos, psicólogos y nutriólogos que nos están ayudando, le realizan la llamada y determinan la periodicidad en la que se va a estar realizando el seguimiento, y así evitamos que las personas estén movilizándose en los espacios públicos”, explicó.<br>
Sin embargo, advirtió que no significa que el objetivo sea dejar a todas y todos siempre en casa, pues en el momento en que sea identificado un riesgo ante el cual la o el paciente deba acudir a una unidad de salud, se le indicará.<br>
“Hasta ahora 113 mil 831 usuarias y usuarios registrados en la plataforma, y 94 mil 736 registros dentro de Salud Digital”, expuso.<br>
Dijo que la diferencia entre estos números, obedece a que una misma persona puede registrar a varios miembros de su familia.<br>
Mencionó que el 81 por ciento de quienes se dieron de alta en la app, no tuvieron COVID-19, aunque si la persona detecta que sus síntomas cambiaron puede actualizarlos y el mecanismo se detona nuevamente desde el principio para evaluarlos.<br>
Hugo Renán Covián, coordinador de los 18 médicos que integran la Gerencia Amarilla de Salud Digital, también participó en la emisión de Chihuahua Adelante y comentó que todo el personal que atiende esta emergencia es experto en detectar la sintomatología de esta enfermedad.<br>
“En la gerencia amarilla, en los últimos 15 días se registraron aproximadamente 350 personas, que requirieron atención telefónica, y a todas ellas se les da seguimiento al 100 por ciento”, comentó.<br>
Dijo que el médico que llama por primera vez a la o el paciente, es quien dará el seguimiento, pero todo el equipo de salud puede participar para que el tratamiento sea integral.<br>
“Al ver las notas del paciente, tal vez yo, como psicólogo, voy a dar seguimiento a alguien que también la gerencia amarilla está viendo, y ahí me doy cuenta de cómo han disminuido los síntomas, para que mi intervención psicológica sea más eficiente”, observó.<br>
Recalcó que el dinamismo de esta aplicación digital agregó un par de preguntas relacionadas con la disposición y uso del oxímetro.<br>
“Nos dimos cuenta de que muchos de nuestros pacientes empezaron a sentir un cansancio o una fatiga muy extrema y pensaron que era algo normal, sin embargo, era un reflejo de que su saturación de oxígeno era muy baja”, compartió.<br>
Una vez que se conoce la cifra que arroja esta herramienta, el personal médico marca como “un poquito alarmante de 94 hacia abajo, pero el paciente puede continuar en su domicilio, siempre y cuando ese saturación no se degrade por debajo de 90, entonces, contar con el oxímetro es muy muy importante”, afirmó.<br>
Salud Digital está disponible para cualquier dispositivo móvil, y se puede descargar de manera gratuita, de las tiendas de aplicaciones de Android y de iOs.<br>
Una vez instalada en el teléfono celular, se ingresa al apartado Regístrate y averigua si eres sospechoso de COVID-19, y recibirás un código de seguridad para escribir tu nombre y datos generales.<br>
La aplicación es segura y toda la información personal ingresada es confidencial.<br>
Para continuar se invita a la persona a llenar un cuestionario de 12 preguntas sobre la sintomatología, y según la cantidad y tipo de respuestas positivas, se cataloga al paciente con un color, para priorizar la atención.<br>
A los grupos amarillo, naranja y rojo se les dará un seguimiento, y se les explica cómo es el proceso para recibir atención y monitoreo.</p>
                            
	                        
                                                    </div>
</div>
                          </div>
                </div>
                        
                              <div class="caja-noticia" data-noticia="2">
                    <h2>Revisan Brigadas de Salud Estatal vulnerabilidad comunitaria ante COVID casa por casa</h2>
                    <img src="https://i2.wp.com/comunicachihuahua.desarrollosenlanube.net/wp-content/uploads/2020/12/revisan-brigadas-de-salud-estatal-vulnerabilidad-comunitaria-ante-covid-casa-por-casa_5fd3d46a7242e.jpeg">
                </div>
                <div class="noticia-cuerpo" id="noti2" style="display: none;">
                    <div class="cerrar-noticia"> <i class="fad fa-arrow-circle-left"></i>  Atrás</div>
                    <img src="https://i2.wp.com/comunicachihuahua.desarrollosenlanube.net/wp-content/uploads/2020/12/revisan-brigadas-de-salud-estatal-vulnerabilidad-comunitaria-ante-covid-casa-por-casa_5fd3d46a7242e.jpeg">
                    <h1>Revisan Brigadas de Salud Estatal vulnerabilidad comunitaria ante COVID casa por casa</h1>
                    <div class="content-inner">
                            <div class="noticia_full">
<div class="jeg_share_button share-float jeg_sticky_share clearfix share-monocrhome">
                                                    </div>

                        <div class="content-inner ">
                            <p>Verónica Carreón Falcón, epidemióloga coordinadora del equipo en el municipio juarense, explica en Chihuahua Adelante, que la estrategia se basa en acudir a colonias de Chihuahua y Juárez donde en los últimos 15 días hubo casos y fallecimientos por esta enfermedad, para identificar síntomas y comorbilidades que pudieran detonar cadenas de transmisión y más decesos Las Brigadas de Atención a Pacientes COVID-19, de la Secretaría de Salud Chihuahua, a diario recorren las diversas colonias de Ciudad Juárez y Chihuahua para medir la vulnerabilidad comunitaria y brindar una intervención temprana que evite cadenas de contagio de esta y otras enfermedades.<br>
Verónica Carreón Falcón, epidemióloga coordinadora del equipo en el municipio juarense, mediante un enlace virtual al programa Chihuahua Adelante, señaló que la estrategia es llegar a cada casa para identificar posibles casos de diversos padecimientos y canalizarlos a unidades de segundo nivel.<br>
Con esto –explicó- se evita que se compliquen y que ocurran decesos por falta de atención médica.<br>
Resaltó que a la fecha hay 12 brigadas que miden la vulnerabilidad comunitaria en cuestión de salud, en Ciudad Juárez, y se trabaja para integrar a más, por medio de la red de Servicios de Salud de la Secretaría de Salud Estatal.<br>
En el marco de la pandemia de COVID-19, el objetivo es identificar a las y los ciudadanos con factores de riesgo de infectarse con Sars-Cov2, como puede ser la hipertensión arterial, diabetes y asma.<br>
De igual manera, las brigadas evalúan la salud materna: “a las embarazadas, es muy importante detectarlas de manera oportuna, para prevenir que vayan a tener un embarazo complicado que pudiera ocasionar la muerte tanto de la madre como del bebé”, indicó.<br>
La epidemióloga dijo que la selección de manzanas a visitar en las colonias, se basa en un sistema de georefernciación que toma en cuenta factores determinantes, como la cantidad de pacientes con COVID, detectados en los últimos 15 días.<br>
“Identificamos las colonias que tienen riesgo, ya sea por el número de casos o por el número de defunciones que ha presentado. Y la finalidad de estas acciones es que la población no se mueva y tenga una menor movilidad para evitar el número de contagios”, comentó.<br>
Compartió que día a día a las 8 la mañana, las brigadas parten de la Jurisdicción Sanitaria correspondiente, con el equipo y personal médico preparado un día anterior.<br>
Destacó que en general la recepción que les ha dado la ciudadanía ha sido buena, pues se ha mostrado dispuesta a recibir la información y recomendaciones.<br>
Explicó que cuando es detectada una persona con sintomatología de COVID-19, se le comunica a una brigada médica especializada, integrada por una enfermera y otras personas que acuden a valorar la condición del paciente, así como a tomar muestras.<br>
La funcionaria recomendó a la población, que en caso de ser necesario, puede llamar al número de atención a emergencias 9-1-1, para ser trasladada a una unidad de segundo nivel.</p>
                            
	                        
                                                    </div>
</div>
                          </div>
                </div>
                        
                              <div class="caja-noticia" data-noticia="3">
                    <h2>Registra Salud 253 nuevos casos y 33 decesos por COVID-19 en el estado</h2>
                    <img src="https://i1.wp.com/comunicachihuahua.desarrollosenlanube.net/wp-content/uploads/2020/12/registra-salud-253-nuevos-casos-y-33-decesos-por-covid-19-en-el-estado_5fd3d0ea3e1c2-scaled.jpeg">
                </div>
                <div class="noticia-cuerpo" id="noti3" style="display: none;">
                    <div class="cerrar-noticia"> <i class="fad fa-arrow-circle-left"></i>  Atrás</div>
                    <img src="https://i1.wp.com/comunicachihuahua.desarrollosenlanube.net/wp-content/uploads/2020/12/registra-salud-253-nuevos-casos-y-33-decesos-por-covid-19-en-el-estado_5fd3d0ea3e1c2-scaled.jpeg">
                    <h1>Registra Salud 253 nuevos casos y 33 decesos por COVID-19 en el estado</h1>
                    <div class="content-inner">
                            <div class="noticia_full">
<div class="jeg_share_button share-float jeg_sticky_share clearfix share-monocrhome">
                                                    </div>

                        <div class="content-inner ">
                            <p>Llama a la población a no bajar la guardia este sábado 12 de diciembre, día que se celebra a la Virgen de Guadalupe; invita a evitar las tradicionales peregrinaciones y celebraciones presencialesLos registros de contagios y defunciones por COVID-19 siguen a la baja en la semana 48, sin embargo aún representan un riesgo para la población, mencionó el director médico de la Secretaría de Salud en la zona norte, Arturo Valenzuela Zorrilla en la conferencia Informativa #294 y Virtual #254 del Reporte COVID-19.<br>
“Seguimos con números descendentes, por fortuna, aún no llegamos al margen de seguridad, sin embargo si nos seguimos esforzando pronto estaremos en condiciones de ir abriendo un poco más la economía”, mencionó.<br>
De esa forma, el total de casos acumulados a la fecha es de 41 mil 730 con 253 nuevos contagios, así como 3 mil 900 personas fallecidas, al registrarse 33 decesos más, de los cuales, 16 fueron confirmados en Juárez, 7 en la ciudad de Chihuahua, 2 en Delicias, 2 en Ahumada, así como uno en cada uno de los siguientes municipios: Parral, Cuauhtémoc, Nuevo Casas Grandes, Madera, Santa Bárbara y Moris.<br>
El funcionario médico llamó a la población a no bajar la guardia este sábado 12 de diciembre, día que se celebra a la Virgen de Guadalupe, por lo que invitó a la feligresía católica a evitar celebraciones presenciales como las tradicionales peregrinaciones.<br>
Precisó que a la fecha van 117 mil 851 inscripciones en la aplicación para celular “Salud Digital”, que tiene como fin registrar y atender casos de COVID-19 en Chihuahua.<br>
Del total de registros 74 mil 313 recibieron en respuesta Gerencias Blanco/Verde, otros 3 mil 423 recibieron atención catalogada como COVID-19 (Amarillo) y 6 mil 207 atención catalogada como COVID-19 (Rojo/Naranja); en cuanto a Monitor Covid, se han sumado 4 mil 150 personas a la lucha de evitar contagios.<br>
Se informó también que se tienen 22 mil 724 (+398) recuperados, 21 mil 575 (+163) descartados y 2,864 (-82) sospechosos.<br>
Mencionó que los contagios por municipio son los siguientes: Ahumada 77, Aldama 97, Allende 70, Ascensión 63, Aquiles Serdán 151, Bachíniva 14, Batopilas 6, Bocoyna 268, Balleza 9, Buenaventura 34, Camargo 285, Carichí 8, Casas Grandes 24, Chihuahua 9,523, Chínipas 115, Coronado 5, Coyame del Sotol 8, Cuauhtémoc 1,312, Cusihuiriachi 13, Delicias 1,628, Dr. Belisario Domínguez 3, Galeana 7, Gómez Farías 68, Guachochi 233, Gran Morelos 8, Guadalupe 14, Guadalupe y Calvo 28, Guazapares 64 y Guerrero 60.<br>
Parral 1,505, Ignacio Zaragoza 12, Janos 18, Jiménez 187, Juárez 23,586, Julimes 9, López 8, Madera 35, Manuel Benavides 25, Matachí 2, Meoqui 219, Moris 4, Namiquipa 67, Nonoava 16, Nuevo Casas Grandes 630, Ocampo 15, Ojinaga 740, Praxedis G. Guerrero 11, Riva Palacio 6, Rosales 59, Rosario 3, San Francisco del Oro 23, Santa Bárbara 61, Satevó 5, Saucillo 169, Temósachic 9, Urique 36, Valle de Zaragoza 11, San Francisco de Conchos 11, Santa Isabel 11, La Cruz 19, San Francisco de Borja 5, Maguarichi 1, El Tule 4, Matamoros 14 y Uruachi 1.<br>
La información muestra que el 51% son del sexo masculino (21,439 casos) y 49% femenino (20,291 casos).<br>
En cuanto a decesos por municipio informó que van 2,291 en Juárez, 771 Chihuahua, 185 Delicias, 141 Parral, 121 Cuauhtémoc, 55 Nuevo Casas Grandes, 41 Meoqui, 39 Camargo, 32 Saucillo, 19 Guerrero, 20 Jiménez, 14 Guachochi, 12 Ascensión, 11 Rosales, 9 Ahumada, 6 Bocoyna, 8 Ojinaga, 5 Carichí, 6 Namiquipa, 5 Temósachic, 7 Aquiles Serdán, 7 Buenaventura, 8 Madera, 6 San Francisco del Oro, 7 Aldama, 5 Casas Grandes, 4 Galeana, 4 Ocampo, 4 Urique, 4 Gómez Farías, 3 Riva Palacio, 3 Janos, 4 Julimes, 3 Coronado y 3 Guadalupe D. B.<br>
Además, 3 en Ignacio Zaragoza, 3 Cusihuiriachi, 2 Dr. Belisario Domínguez, 3 Coyame del Sotol, 2 Moris, 1 Allende, 2 Balleza, 1 Matachí, 1 Bachíniva, 1 Guazapares, 2 Valle de Zaragoza, 1 Santa Isabel, 3 López, 3 San Francisco de Conchos, 4 Santa Bárbara, 2 Guadalupe y Calvo, 1 Gran Morelos, 1 Nonoava y 1 El Tule.<br>
Edades de pacientes fallecidos: 6 casos menores a un año; 2 de 1 a 4; 2 de 5 a 9; 3 de 10 a 14; 2 de 15 a 19; 16 de 20 a 24; 33 de 25 a 29; 68 de 30 a 34; 87de 35 a 39; 192 de 40 a 44; 290 de 45 a 49; 386 de 50 a 54; 474 de 55 a 59; 543 de 60 a 64; 479 de 65 a 69; 471 de 70 a 74; 388 de 75 a 79; 272 de 80 a 84; 121 de 85 a 89; 46 de 90 a 94; 16 de 95 a 99 y 3 de 100 a 104 años de edad.<br>
Porcentajes de comorbilidad en fallecimientos: 34% hipertensión, 25% diabetes, 16% obesidad, 6% tabaquismo, 6% otra condición, 4% enfermedad cardiaca, 4% insuficiencia renal, 2% EPOC, 2% inmunosupresión, 1% asma, 0.3% VIH/Sida. La proporción es 39% mujeres y 61% hombres.<br>
En este momento el estado tiene 405 pacientes hospitalizados: 56% en el IMSS, 24% en el Sector Salud, 6% en el Issste, 13% en Sedena, 1% en IMSS Bienestar. De esos, 96 están intubados, 52% en el IMSS, 39% en SSA, 7% en el Issste y 2% en Sedena. Con reporte de 29 hospitales.<br>
Muestras de diagnóstico: Laboratorio Estatal 81, acumuladas 31,774; otros laboratorios 400, acumuladas 100,490; total de muestras 481, acumuladas 132,234.<br>
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
                    <div class="cerrar-noticia"> <i class="fad fa-arrow-circle-left"></i>  Atrás</div>
                    <img src="https://i2.wp.com/comunicachihuahua.desarrollosenlanube.net/wp-content/uploads/2020/12/posicionamiento-de-la-seyd-sobre-los-centros-comunitarios-de-aprendizaje_5fd3bf5256bf7.jpeg">
                    <h1>Posicionamiento de la SEyD sobre los Centros Comunitarios de Aprendizaje</h1>
                    <div class="content-inner">
                            <div class="noticia_full">
<div class="jeg_share_button share-float jeg_sticky_share clearfix share-monocrhome">
                                                    </div>

                        <div class="content-inner ">
                            <p>En ese tenor, Chihuahua reinicia la planeación de la estrategia local denominada “Centros de Asesoría y Acompañamiento”, para cuando las diversas regiones de la entidad se encuentren en semáforo epidemiológico color amarillo; pero ya sin considerarlo como un pilotaje, sino como una estrategia general y nacionalDurante la LI Sesión del Consejo Nacional de Autoridades Educativas, CONAEDU, el Secretario de Educación Pública del Gobierno de México, Esteban Moctezuma Barragán, reiteró el  de la estrategia de los Centros Comunitarios de Aprendizaje como una estrategia previa a un eventual re de clases presenciales, en la que se tomarán en cuenta los siguientes factores:<br>
 ¿	Semáforo de Riesgo Epidemiológico en color amarillo, mismo que permite una mayor movilidad social con medidas de prevención. En este nivel, muchas actividades económicas, sociales y culturales son aperturadas con porcentajes de asistencia, lo que hace previsible el  de un modelo especial para las escuelas ubicadas en dichas regiones. ¿	Actividad de carácter voluntaria de maestras y maestros, lo que permite considerar aquellas escuelas cuyos docentes estén en circunstancias de salud que les permita participar sin riesgos. ¿	Horarios restringidos, considerando que la actividad principal de estos Centros sería el acompañamiento, asesoría y reforzamiento académico de los alumnos que así lo requieran, al igual que la atención a las madres y padres de familia. ¿	Acciones previas de limpieza e higienización de los centros escolares. ¿	Capacidad limitada de atención diaria a alumnas, alumnos y en su caso, madres y padres de familia o tutores, con la posibilidad de generar estrategias de atención por días específicos a alumnos con requerimientos de atención especiales.<br>
En ese sentido, los Centros Comunitarios de Aprendizaje no implican la apertura de todas las escuelas ni mucho menos un re de actividades presenciales académicas regulares en semáforo amarillo. Solamente responden a una realidad en la que la movilidad es mucho más amplia en todas las personas, incluidos quienes inciden en el hecho educativo.<br>
Es importante en el caso de Chihuahua, señalar lo siguiente:<br>
Desde el pasado día 14 de octubre, en comparecencia ante el H. Congreso del Estado, la Secretaría de Educación y Deporte (SEyD) informó de una estrategia local para iniciar un plan piloto en diversas escuelas de la entidad, públicas y privadas, rurales, urbanas e indígenas, con el propósito de iniciar en ellas lo que entonces se denominó “Centros de Asesoría y Acompañamiento”, bajo las mismas premisas generales que hoy avala la SEP y en nuestro caso, tomando en consideración dos acciones:<br>
 ¿	Que el programa “Aprende en Casa II” no estaba teniendo la proyección y la efectividad prevista, toda vez que en el territorio estatal la cobertura de la señal de televisión abierta alcanza un 60%, lo que implica la necesidad de desarrollar otras acciones paralelas para el reforzamiento académico. ¿	Que el modelo nacional no es aplicable en sectores específicos de la comunidad chihuahuense como lo son las escuelas indígenas y menonitas, tanto por condicionantes socioculturales como por razones de idioma. ¿	Que en la primera encuesta aplicada a docentes de Educación Básica con cierre al 13 de octubre de 2020, un 40% de las maestras y los maestros afirmó estar realizando actividades de presencialidad con sus alumnos con el fin de apoyarlos en el proceso educativo y reforzar los contenidos académicos. Estas acciones, de acuerdo a lo indicado en la encuesta, derivan en el acercamiento de las y los docentes con sus alumnos en espacios no escolares, toda vez que éstos permanecen cerrados a cualquier actividad desde el mes de marzo del presente año. ¿	Que de acuerdo a los parámetros de las autoridades sanitarias, el semáforo amarillo implica una mayor movilización social y permite la apertura de actividades presenciales en todos los órdenes y niveles, aplicando una serie de medidas preventivas. En esa etapa, todas las actividades aumentan sus porcentajes de atención y la movilidad es más generalizada, lo que de suyo permite la apertura de los edificios escolares para brindar cierto tipo de servicios educativos como las asesorías y el acompañamiento en un esquema de atención presencial, escalonado y limitado, tanto a alumnos como a madres y padres de familia, en su caso.<br>
La regresión en el semáforo epidemiológico impidió la concreción de este Plan Piloto de la SEyD, que en un primer momento consideraba hasta a 30 escuelas de educación básica en todo el territorio estatal. Sin embargo, desde el mes de noviembre pasado, la autoridad educativa nacional expuso la necesidad de iniciar con un modelo de transición a la normalización de las actividades educativas, lo que finalmente fue informado el día de ayer bajo el mismo esquema y condiciones como en su tiempo se planteó para el Estado de Chihuahua.<br>
En ese tenor, la Secretaría de Educación y Deporte informa que reinicia la planeación de esta estrategia para cuando las diversas regiones de la entidad se encuentren en semáforo epidemiológico color amarillo, pero ya sin considerarlo como un pilotaje, sino como una estrategia general y nacional que nos permita abordar de manera más directa el proceso de enseñanza aprendizaje bajo los criterios sanitarios imperantes y con las consideraciones del Sector Salud. En ello, se dará prioridad a las regiones de mayor riesgo y vulnerabilidad.</p>
                            
	                        
                                                    </div>
</div>
                          </div>
                </div>
                        
                              <div class="caja-noticia" data-noticia="5">
                    <h2>Explica Salud estrategia desplegada para atender la pandemia por COVID-19 en Chihuahua</h2>
                    <img src="https://i1.wp.com/comunicachihuahua.desarrollosenlanube.net/wp-content/uploads/2020/12/explica-salud-estrategia-desplegada-para-atender-la-pandemia-por-covid-19-en-chihuahua_5fd3b64256f41.jpeg">
                </div>
                <div class="noticia-cuerpo" id="noti5" style="display: none;">
                    <div class="cerrar-noticia"> <i class="fad fa-arrow-circle-left"></i>  Atrás</div>
                    <img src="https://i1.wp.com/comunicachihuahua.desarrollosenlanube.net/wp-content/uploads/2020/12/explica-salud-estrategia-desplegada-para-atender-la-pandemia-por-covid-19-en-chihuahua_5fd3b64256f41.jpeg">
                    <h1>Explica Salud estrategia desplegada para atender la pandemia por COVID-19 en Chihuahua</h1>
                    <div class="content-inner">
                            <div class="noticia_full">
<div class="jeg_share_button share-float jeg_sticky_share clearfix share-monocrhome">
                                                    </div>

                        <div class="content-inner ">
                            <p>La premisa ha sido salvar el mayor número de vidas y cortar la red de contagios; se impulsaron 13 políticas públicas, plataformas digitales, capacitaciones y los 10 pasos de la salud para la prevención de la enfermedadBajo la premisa de salvar el mayor número de vidas posibles con acciones oportunas de diagnóstico, aislamiento, seguimiento y atención de casos, así como mantener los niveles de contagio COVID-19 en zona segura para la ocupación hospitalaria y romper las cadenas de riesgo, la Secretaría de Salud del Gobierno del Estado desplegó una amplia estrategia para contener la pandemia en Chihuahua.<br>
En ella, la corresponsabilidad sociedad y Gobierno es fundamental para mitigar los efectos tanto en la salud como en la economía, expresó la subsecretaria de Prevención y Promoción de la Salud. Mirna Beltrán Arzaga, en el programa Chihuahua Adelante.<br>
Al explicar en qué consisten las acciones desplegadas desde que se detectó la enfermedad y posteriormente cuando se decretó la pandemia, la funcionaria a cargo de la estrategia indicó cómo se ha llegado a algunos límites y cómo se ha superado para seguir brindando la atención adecuada en hospitales y de manera preventiva.<br>
Los objetivos son muy puntuales y el principal es salvar vidas, eso es indiscutible lo que ha llevado a crear diferentes políticas públicas que son las que ayudan a un control de esta pandemia y “algo muy importante es crear ese vínculo y esa corresponsabilidad entre gobiernos y población”, expresó.<br>
Explicó que desde enero que se conoció la existencia del nuevo coronavirus, empezaron a reunirse los diferentes grupos al interior de la Secretaría de Salud para ir analizando y creando la estrategia, donde las primeras acciones son de promoción, prevención, vigilancia epidemiológica y la atención médica, de diagnóstico y aislamiento.<br>
Estas son acciones esenciales para evitar que las personas lleguen a los hospitales y en las que en el centro siempre debe estar la comunidad, es decir, “las personas son nuestro eje fundamental para llevar a cabo las acciones, los planes y la orientación adecuada”.<br>
Está el primer contacto con el sistema de salud a través del 9-1-1 (911) y la plataforma Salud Digital, donde se hace la identificación de casos sospechosos y seguimiento por medio de video llamadas o tele consultas de casos positivos.<br>
Las acciones de promoción de la salud diariamente en las conferencias de prensa por la mañana, donde se informa cómo va evolucionando la pandemia y las acciones necesarias para que la gente tome las mejores decisiones preventivas.<br>
Luego está la atención primaria, que es cuando las personas llegan a una unidad de primer nivel para ser diagnosticados e interrogados mediante el estudio epidemiológico que se realiza para hacer el rastreo de sus contactos más cercanos e iniciar la atención médica.<br>
Posteriormente se trabaja en la atención temprana del segundo nivel que es en los hospitales para evitar que la gente llegue con algún grado de complicación y pueda desencadenar en una defunción.<br>
Otra parte de la estrategia la constituye la Red Chihuahuense de Municipios por la Salud, la cual y tiene varios años pero ahora ha sido importante tanto en la prevención como en la atención de casos, ya que son las autoridades municipales el primer contacto con la población quienes más conocen de la dinámica, del entorno y de las enfermedades.<br>
Son ellos, señaló la Dra. Beltrán, los encargados de minimizar la vulnerabilidad que existe por otro tipo de determinantes sociales de la salud como son el acceso al empleo, a los servicios básicos de agua, drenaje, educación y todo esto, en conjunto con las herramientas que les brindamos de cómo cuidar a su población.<br>
De igual manera, las jurisdicciones sanitarias se reúnen con las y los presidentes municipales y sus equipos, para analizar por medio de los diagnósticos, la problemática de salud que se está presentando en cada uno y ahí se toman las decisiones y las acciones necesarias.<br>
Al respecto, Beltrán Arzaga indicó que en los próximos días, los 67 alcaldes presentarán un informe de todas las acciones que han realizado ante la pandemia, los resultados y el impacto que se ha tenido en los municipios.<br>
Informó que se han impulsado 13 políticas públicas que están instaladas dentro de los diferentes acuerdos emitidos a lo largo de la pandemia y que se constituyen como un instructivo para ir creando las actividades y las acciones preventivas y activas.<br>
Dentro de esas acciones destacó el vínculo con el Tecnológico de Monterrey y con la Universidad Autónoma de Chihuahua, quienes a través de sus investigadores han apoyado para la generación de diferentes herramientas que permiten tomar las mejores decisiones, gracias a la georreferenciación, plataforma que sirve para identificar puntos focales y locales de concentración de casos y el emprendimiento de acciones.<br>
Se han adherido más de más de 4 mil Monitores COVID y se hace la invitación para que más gente se integre a esta gran estrategia de corresponsabilidad para evitar los contagios en los centros de trabajo o haciendo una compra.<br>
Se ha intervenido en más de 11 mil entornos a través de diferentes capacitaciones virtuales: más de 10,000 trabajadores de la salud y más de 11 mil empleadas y empleados de las diferentes dependencias de gobierno y del sector privado.<br>
Más de 2 mil protocolos han sido revisados y se siguen haciendo porque hay empresas que siguen actualizándose e incluso empresas que todavía no aperturan ya están enviando sus protocolos para estar listos en el momento en el que puedan reabrir.<br>
Los programas básicos que son la vacunación y prevención de enfermedades crónico degenerativas; son 33 programas preventivos que maneja la Secretaría de Salud a través de sus 11 jurisdicciones sanitarias.<br>
Además se cuenta con los 10 pasos de la Brigada de Promoción de la Salud, dirigida a la población: 1. Evaluar la vulnerabilidad comunitaria; 2.Identificar personas en riesgo; 3. Reducir el riesgo de complicarse y morir por COVID-19; 4. Detectar tempranamente a personas enfermas; 5. Otorgar seguimiento estrecho; 6. Brindar atención integral de la salud; 7. Realizar referencias oportunas para la atención; 8. Detectar, estudiar y controlar brotes comunitarios; 9. Dar soporte social solidario y 10. Continuar la atención general en salud.<br>
Otra de las acciones destacadas son las Brigadas de Promoción de la Salud que contaron en principio con el apoyo del Salud federal pero que fue retirado por la contingencia por las lluvias en Tabasco. Con esta acción se ha llegado al menos a 24 mil habitantes de los diferentes municipios del estado.<br>
Se anexan las gráficas con los detalles que apoyan la estrategia de la Secretaría de Salud del Gobierno del Estado.</p>
                            
	                        
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
                        <i class="fad fa-stethoscope"></i> Hipertensión
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
            ¿Desearia compartir sus datos de movilidad con los demas usuarios para asi poder identificar posibles nuevos casos?
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




