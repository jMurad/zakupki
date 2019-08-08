from bs4 import BeautifulSoup
import re


docs_html = '''<html><head>
  <meta http-equiv="content-type" content="text/html; charset=UTF-8">
  <link href="https://fonts.googleapis.com/css?family=Roboto+Slab:400,700&amp;subset=latin,cyrillic" rel="stylesheet" type="text/css">

  <title>Сведения закупки</title>

  <script type="text/javascript" async="" src="https://mc.yandex.ru/metrika/watch.js"></script><script type="text/javascript">
      var contextPath = "/epz/order/notice";
  </script>

  
    
    
      <link type="text/css" rel="stylesheet" media="all" href="/epz/order/notice/css/style.css">
      <link type="text/css" rel="stylesheet" href="/epz/order/notice/css/jquery_msgbox.css">
    
  

  <script type="text/javascript" src="/epz/order/notice/js/jquery-3.3.1.min.js"></script>
  <script type="text/javascript" src="/epz/order/notice/js/jquery.cookie.min.js"></script>
  <script type="text/javascript" src="/epz/order/notice/js/js.cookie.js"></script>
  <script type="text/javascript" src="/epz/order/notice/js/jquery_msgBox.js"></script>
  <script type="text/javascript">
      function sessionTimeOutMsg(){
          $.msgBox({
              type:"error",
              content:"Время ожидания соединения истекло",
              title: "Сообщение",
              afterClose: function(result) {
                  document.location.href = ""
              }
          });
      }
    
      var isRegisteredUserObozApp = Boolean("");
      var sessionMaxInactiveInterval = "";      
      $(document).ready(function(){
          var notUsual = (($.cookie("usePoorVisionOption") == 'true') && $(".goodVisionLink").length == 0);
          var notPoorVision = (($.cookie("usePoorVisionOption") != 'true') && $(".poorVisionLink").length == 0);
          if (notUsual || notPoorVision){
              location.reload();
          }
      });
  </script>
  <script>window.jQuery || document.write('<script src="/epz/order/notice/js/jquery-3.3.1.min.js"><\/script>')</script>
  <script type="text/javascript" src="/epz/order/notice/js/ui_autocomplete.js"></script>
  
  
  <script type="text/javascript" src="/epz/order/notice/js/mustache.min.js"></script>
  <script type="text/javascript" src="/epz/order/notice/js/jquery.price_format.1.7.js"></script>
  
  <script type="text/javascript" src="/epz/order/notice/js/moment.min.js"></script>
  <script type="text/javascript" src="/epz/order/notice/js/moment-timezone.min.js"></script>

  <script type="text/javascript" src="/epz/order/notice/js/action-switch.js"></script>
  <script type="text/javascript" src="/epz/order/notice/js/browser.js"></script>

  <script type="text/javascript" src="/epz/order/notice/js/script.js"></script>
  <script type="text/javascript" src="/epz/order/notice/js/cards_keyboard_control_script.js"></script>
  <script type="text/javascript" src="/epz/order/notice/js/custom.js"></script>
  <script type="text/javascript" src="/epz/order/notice/js/URI.js"></script>
  <script type="text/javascript" src="/epz/order/notice/js/common/config.js"></script>
  <script type="text/javascript" src="/epz/order/notice/js/common/analytics.js"></script>
  <script type="text/javascript" src="/epz/order/notice/js/cardBaseLayout.js"></script>
  
      
      
          <script type="text/javascript" src="/epz/order/notice/js/keyboardNavigationRules.js"></script>
      
  
  <script type="text/javascript" src="/epz/order/notice/js/keyboardControl.js"></script>
  <script type="text/javascript" src="/epz/order/notice/js/jquery-migrate-3.0.1.min.js"></script>
  <script type="text/javascript">
      var contextPath = "/epz/order/notice";
      var epzMainPublicUrl = "/epz/main/public/";
  </script>
  <script type="text/javascript" src="/epz/order/notice/js/checkNotice.js"></script>
  



<script type="text/javascript">
    epzCommonConfig.initCommonConfig({
        contextPath: '/epz/order/notice',
        smartSearchEnable: true,

        urls: {
            epzMainPublicUrl: '/epz/main/public/',
            epzNsiUrl: '/epz/nsi/',
            epzOrderUrl: '/epz/order/',
            epzOrderPlanUrl: '/epz/orderplan/',
            epzOrderClauseUrl: '/epz/orderclause/',
            epzContractUrl: '/epz/contract/',
            epzContractFz223Url: '/epz/contractfz223/',
            epzContractReportingUrl: '/epz/contractreporting/',
            epzCustomerReportsUrl: '/epz/customerreports/',
            epzOrganizationUrl: '/epz/organization/',
            epzDishonestSupplierUrl: '/epz/dishonestsupplier/',
            epzComplaintUrl: '/epz/complaint/',
            epzBankGuaranteeUrl: '/epz/bankguarantee/',
            epzInspectionPlanUrl: '/epz/inspectionplan/',
            epzUnscheduledInspectionUrl: '/epz/unscheduledinspection/',
            epzControlResultUrl: '/epz/controlresult/',
            epzDizkUrl: '/epz/dizk/',
            epzEsUrl: '/analytics/hit/',
            epzFarmUrl: '/epz/farm/'
        }
    });
</script>
  

<!-- Yandex.Metrika counter -->
<script type="text/javascript">
    (function (d, w, c) {
        (w[c] = w[c] || []).push(function() {
            try {
                w.yaCounter36706425 = new Ya.Metrika({
                    id:36706425,
                    clickmap:true,
                    trackLinks:true,
                    accurateTrackBounce:true
                });
            } catch(e) { }
        });

        var n = d.getElementsByTagName("script")[0],
                s = d.createElement("script"),
                f = function () { n.parentNode.insertBefore(s, n); };
        s.type = "text/javascript";
        s.async = true;
        s.src = "https://mc.yandex.ru/metrika/watch.js";

        if (w.opera == "[object Opera]") {
            d.addEventListener("DOMContentLoaded", f, false);
        } else { f(); }
    })(document, window, "yandex_metrika_callbacks");

    function yandexCounterHit(url) {
        if (typeof(yaCounter36706425) != "undefined") {
            yaCounter36706425.hit(url);
        }
    }

    $(document).ready(function () {
        $("a[target=_blank]:not([initialHref])").click(function (event) {
            yandexCounterHit($(this).attr("href"));
        });

        $(document).ajaxSend(function (event, request, settings) {
            yandexCounterHit(settings.url);
        });
    });

</script>
<noscript><div><img src="https://mc.yandex.ru/watch/36706425" style="position:absolute; left:-9999px;" alt="" /></div></noscript>
<!-- /Yandex.Metrika counter -->


</head>
<body class="cardLayout">

<script type="text/javascript">
  if ($.cookie('usePoorVisionOption') === 'true') {
    var body = $('body');
    var style = '';
    var cookie = $.cookie('colorSpectrumForPoorVision');
    if (cookie) {
      body.addClass(cookie + 'ColorSpectrum');
      switch (cookie) {
        case 'white':
          style = '#ffffff';
          break;
        case 'black':
          style = '#000000';
          break;
        case 'blue':
          style = '#9DD1FF';
          break;
        case 'brown':
          style = '#442713';
          break;
        case 'biege':
          style = '#F7F3D6';
          break;
        default:
          break;
      }
      body.css({backgroundColor: style});
    }

    var fontZize = $.cookie('fontSizeForPoorVision');
    if (fontZize) {
      body.addClass('fontSizeForPoorVision' + fontZize);
    }
  }
</script>

<div class="cardWrapper outerWrapper">

  <div class="wrapper">

    <div class="mainBox">
      






<script type="text/javascript">
    $(document).ready(function () {
        var poorVisionSettingsBlock = $('.poorVisionSettingsBlock');

        
        
        
        var poorVisionLink = poorVisionSettingsBlock.find('.poorVisionLink');

        poorVisionLink.click(function (e) {
            e.preventDefault();
            $.cookie('usePoorVisionOption', 'true', {path: '/', expires: 365*100});
            location.reload();
        });
        
        
    });

</script>

<div class="poorVisionSettingsBlock">
    
        
        
            <span>
                <a class="poorVisionLink poorVisionBannerCards"></a>
            </span>
        
    
</div>
      






















<div class="cardHeader">
    <a href="/epz/main/public/home.html" class="cardLogo"></a>
    <h1 class="padBtm8">Закупка №0153300061119000017
        <sup>
            
                
                
                    <a target="_blank" title="RSS-подписка на события закупки" href="/epz/order/notice/rss?regNumber=0153300061119000017">rss</a>
                
            
        </sup>
    </h1>

    
    <div class="public">
        
        Размещено: 28.06.2019 15:29 (MSK+2 (UTC+5) Екатеринбург) <br>По местному времени организации, осуществляющей закупку
    </div>
</div>


      



























<div class="contentTabs noticeTabs">
    <table class="contentTabsWrapper">
        <tbody><tr>
            













    <td tab="MAIN_INFO" parent="" url="/epz/order/notice/zk504/view/common-info.html?regNumber=0153300061119000017" class="">
        
            
            
            
                
            
        
        <div class="td-overflow"><span class="td-content"><span>Общая информация</span></span></div>
    </td>



            















            













    <td tab="PURCHASE_DOCS" parent="" url="/epz/order/notice/zk504/view/documents.html?regNumber=0153300061119000017" class="currentTab">
        
            
            
            
                
            
        
        <div class="td-overflow"><span class="td-content"><span>Документы закупки</span></span></div>
    </td>



            

            
                













    <td tab="SUPPLIER_RESULTS" parent="" url="/epz/order/notice/zk504/view/supplier-results.html?regNumber=0153300061119000017" class="">
        
            
            
            
                
            
        
        <div class="td-overflow"><span class="td-content"><span>Результаты определения поставщика</span></span></div>
    </td>


            

            













    <td tab="EVENT_LOG" parent="" url="/epz/order/notice/zk504/view/event-journal.html?regNumber=0153300061119000017" class="">
        
            
            
            
                
            
        
        <div class="td-overflow"><span class="td-content"><span>Журнал событий</span></span></div>
    </td>


        </tr>
    </tbody></table>
</div>


    <div class="padBtm20 contentHeadingWrapper" style="width: 620.641px;">
        
            <a target="_blank" class="size14" href="/epz/order/notice/printForm/view.html?printFormId=95910449">
                
                    
                        Извещение о проведении запроса котировок в электронной форме
                    
                    
                    
                
                от 28.06.2019 №0153300061119000017
            </a>
            <br>
        
    </div>


<script>
    $(document).ready(function () {
        $('.contentTabsWrapper td[tab = "PURCHASE_DOCS"]').addClass('currentTab');
        
            if ($('.contentTabsWrapper tr').width() > 980 && false) {
                $('[tab="EVENT_LOG"]').css('display', 'none');
            }
        
        
        
        
        
        
        
    });
</script>


      























<script type="text/javascript" src="/epz/order/notice/js/card/view/documentsButtonPanelNew.js"></script>

    
        <div class="padBtm20 revisionToggleWrapper">
            <div id="hide-editions">
                <span class="block-icon"></span>
                <a id="revisionViewToggle" href="javascript:toggleActiveRevisionView()">Отобразить недействующие
                    редакции</a>
            </div>
        </div>
    

<br class="clear">

<div class="contentTabBoxBlock">
    <div class="noticeTabBox padBtm20">
        <h2>Извещение, изменение извещения о проведении запроса котировок в электронной форме</h2>
        <div class="noticeTabBoxWrapper notice-documents padding-0-15px-15px-5px">
            <table>
                <tbody>
                

















    
    
        
        
            













    
    
        <tr class="  ">
            <td class="padRight5 width26px width165pxPV alignCenter">
                
                    <a class="linkPopUp pWidth_840 cryptoSigns" href="/epz/order/notice/signview/list.html?printFormId=95910449"></a>
                
            </td>
            
                <td class="width26px padLeft0 width165pxPV alignCenter">
                    <a class="printForm " href="/epz/order/notice/printForm/view.html?printFormId=95910449" title="Печатная форма" target="_blank"></a>
                </td>
            
            <td class="width_25_pr colorBlack  ">
                
                    
                    
                    
                        Извещение о проведении запроса котировок в электронной форме от 28.06.2019 №0153300061119000017
                    
                
            </td>
            <td class="width_35_pr ">
                
                    <div class="white-space-nowrap">
                        <span>Размещено</span>
                        <span class="white-space-nowrap padLeft10 floatRight">
                                    28.06.2019 15:29 <span class="timeZoneName" title="Екатеринбург">(МСК+2)</span>
                                </span>
                    </div>
                
                <span class="">
                                Действующая редакция
                                
                        </span>

                
            </td>
            <td class="width_30_pr ">
                
                    <div class=" cursorPointer" id="attachmentViewToggle" style="display: none;">
                        <span class="block-icon"></span>
                        <span class="empty">Показать все файлы</span>
                    </div>
                    
                        
                        <div class=" attachment">
                            <div class="white-space-nowrap floatLeft padRight5">
                                    <span class="vAlignMiddle margRight5 successCheckAntivirus" title="Проведена проверка на вирусы"></span>
                                
                                    <a class="linkPopUp pWidth_840 vAlignMiddle margRight5  cryptoSignsSmall" href="/epz/order/notice/signview/list.html?attachmentId=64579816">
                                    </a>
                                
                                <img alt="Microsoft Word Document" src="/epz/order/notice/images/icons/doc.png" class="vAlignMiddle margRight5" title="Microsoft Word Document">
                            </div>
                            <div class="displayTable">
                                <a class="" href="http://zakupki.gov.ru/44fz/filestore/public/1.0/download/priz/file.html?uid=8BE7A3FC48AD0058E0530A86121F6FAA" title="документация.docx">
                                        документация
                                        </a>
                            </div>
                            <div class="clear"></div>
                        </div>
                    
                
            </td>
        </tr>
    

            
                
                
                
                
                    
                    













    
    
        <tr class="  darkBackground">
            <td class="padRight5 width26px width165pxPV alignCenter">
                
                    <a class="linkPopUp pWidth_840 cryptoSigns" href="/epz/order/notice/signview/list.html?printFormId=95923357"></a>
                
            </td>
            
                <td class="width26px padLeft0 width165pxPV alignCenter">
                    <a class="printForm " href="/epz/order/notice/printForm/view.html?printFormId=95923357" title="Печатная форма" target="_blank"></a>
                </td>
            
            <td class="width_25_pr colorBlack  ">
                
                    
                        <a href="/epz/order/notice/printForm/view.html?printFormId=95923357" target="_blank">Уведомление о соответствии контролируемой информации</a>
                    
                    
                    
                
            </td>
            <td class="width_25_pr ">
                
                    <div class="white-space-nowrap">
                        <span>Размещено</span>
                        <span class="white-space-nowrap padLeft10 floatRight">
                                    28.06.2019 13:29
                                </span>
                    </div>
                
                <span class="">
                                
                                
                        </span>

                
                    <div class="white-space-nowrap">
                        <span>Орган контроля по ч.5 ст. 99:</span> <span class="floatLeft white-space-nowrap padLeft10">
                                  ФИНАНСОВЫЙ ОТДЕЛ МЕСТНОЙ АДМИНИСТРАЦИИ КВАРКЕНСКОГО РАЙОНА
                        </span>
                    </div>
                
            </td>
            <td class="width_25_pr ">
                
            </td>
        </tr>
    

                    
                
            
        
    

                </tbody>
            </table>
        </div>

        <h2>Изменение организации, осуществляющей размещение</h2>
        <div class="noticeTabBoxWrapper notice-documents padding-0-15px-15px-5px">
            <table>
                <tbody>
                

















    
        <tr>
            <td>
                
                    Сведения отсутствуют
                
                    
            </td>
        </tr>
    
    

                </tbody>
            </table>
        </div>

        <h2>Квитанции результатов согласования извещения на проведение запроса котировок в электронной форме</h2>
        <div class="noticeTabBoxWrapper notice-documents padding-0-15px-15px-5px">
            <table>
                <tbody>
                

















    
        <tr>
            <td>
                
                    Сведения отсутствуют
                
                    
            </td>
        </tr>
    
    

                </tbody>
            </table>
        </div>

        <h2>Отмена определения поставщика (подрядчика, исполнителя)</h2>
        <div class="noticeTabBoxWrapper notice-documents padding-0-15px-15px-5px">
            <table>
                <tbody>
                

















    
        <tr>
            <td>
                
                    Сведения отсутствуют
                
                    
            </td>
        </tr>
    
    

                </tbody>
            </table>
        </div>

        <h2>Протоколы работы комиссии, полученные с электронной площадки (ЭП)</h2>
        <div class="noticeTabBoxWrapper notice-documents padding-0-15px-15px-5px">
            <table>
                <tbody>
                












    
    
        
            
            <tr class=" ">
                <td class="width_30_pr colorBlack ">
                    
                        
                        
                            <a href="/epz/order/notice/zk504/view/protocol/protocol-main-info.html?regNumber=0153300061119000017&amp;protocolId=24453897">Протокол рассмотрения и оценки заявок на участие в запросе котировок в электронной форме от 10.07.2019 №ПРО1</a>
                        
                        
                        
                    
                </td>
                <td class="width_30_pr">
                    
                        <div class="white-space-nowrap">
                            <span>Размещено на ЭП</span>
                            <span class="white-space-nowrap padLeft10">
                                10.07.2019 17:16 <span class="timeZoneName" title="Екатеринбург">(МСК+2)</span>
                            </span>
                        </div>
                    
                    
                    <div class="white-space-nowrap">
                        <span>Размещено в ЕИС</span>
                        <span class="white-space-nowrap padLeft10">
                            10.07.2019 17:16 <span class="timeZoneName" title="Екатеринбург">(МСК+2)</span>
                        </span>
                        
                    </div>
                    <span>Действующая редакция</span>
                </td>
                <td class="width_30_pr">
                    
                        <div class=" cursorPointer" id="attachmentViewToggle" style="display: none;">
                            <span class="block-icon"></span>
                            <span>Показать все файлы</span>
                        </div>
                        
                            
                            <div class=" attachment">
                                <div class="white-space-nowrap floatLeft padRight5">
                                    <span class="vAlignMiddle margRight5 successCheckAntivirus" title="Проведена проверка на вирусы"></span>
                                    
                                    <img alt="Текстовый документ" src="/epz/order/notice/images/icons/txt.png" class="vAlignMiddle margRight5" title="Текстовый документ">
                                </div>
                                <div class="displayTable">
                                    <a href="http://zakupki.gov.ru/44fz/filestore/public/1.0/download/priz/file.html?uid=8B25D1DA42BD4F26BC1E180736E871B1" class="" title="Электронный документ, полученный из внешней системы.xml ()">
                                            Электронный документ
                                            ...
                                    </a>
                                </div>
                                <div style="clear:both"></div>
                            </div>
                        
                            
                            <div class=" attachment">
                                <div class="white-space-nowrap floatLeft padRight5">
                                    <span class="vAlignMiddle margRight5 successCheckAntivirus" title="Проведена проверка на вирусы"></span>
                                    
                                    <img alt="Microsoft Word Document" src="/epz/order/notice/images/icons/doc.png" class="vAlignMiddle margRight5" title="Microsoft Word Document">
                                </div>
                                <div class="displayTable">
                                    <a href="http://zakupki.gov.ru/44fz/filestore/public/1.0/download/priz/file.html?uid=0B2B9091EBCD4D858A6637D6CED282C5" class="" title="Протокол рассмотрения заявок по запросу котировок17.docx ()">
                                            Протокол рассмотрени
                                            ...
                                    </a>
                                </div>
                                <div style="clear:both"></div>
                            </div>
                        
                    
                </td>
            </tr>
        
            
            <tr class=" ">
                <td class="width_30_pr colorBlack ">
                    
                        
                        
                            <a href="/epz/order/notice/zk504/view/protocol/protocol-main-info.html?regNumber=0153300061119000017&amp;protocolId=24626359">Протокол признания участника уклонившимся от заключения контракта от 23.07.2019 №ППУ1</a>
                        
                        
                        
                    
                </td>
                <td class="width_30_pr">
                    
                    
                    <div class="white-space-nowrap">
                        <span>Размещено в ЕИС</span>
                        <span class="white-space-nowrap padLeft10">
                            23.07.2019 16:50 <span class="timeZoneName" title="Екатеринбург">(МСК+2)</span>
                        </span>
                        
                    </div>
                    <span>Действующая редакция</span>
                </td>
                <td class="width_30_pr">
                    
                        <div class=" cursorPointer" id="attachmentViewToggle" style="display: none;">
                            <span class="block-icon"></span>
                            <span>Показать все файлы</span>
                        </div>
                        
                            
                            <div class=" attachment">
                                <div class="white-space-nowrap floatLeft padRight5">
                                    <span class="vAlignMiddle margRight5 successCheckAntivirus" title="Проведена проверка на вирусы"></span>
                                    
                                        <a class="linkPopUp pWidth_840 vAlignMiddle margRight5 cryptoSignsSmall" href="/epz/order/notice/signview/list.html?attachmentId=66043800"></a>
                                    
                                    <img alt="Microsoft Word Document" src="/epz/order/notice/images/icons/doc.png" class="vAlignMiddle margRight5" title="Microsoft Word Document">
                                </div>
                                <div class="displayTable">
                                    <a href="http://zakupki.gov.ru/44fz/filestore/public/1.0/download/priz/file.html?uid=8E46F9E0157A00FAE0530A86121F6617" class="" title="Протокол признания участника уклонившимся от заключения контракта.docx ()">
                                            Протокол признания у
                                            ...
                                    </a>
                                </div>
                                <div style="clear:both"></div>
                            </div>
                        
                    
                </td>
            </tr>
        
    

                </tbody>
            </table>
        </div>

        <h2>Продление срока подачи заявок на участие в запросе котировок в электронной форме</h2>
        <div class="noticeTabBoxWrapper notice-documents padding-0-15px-15px-5px">
            <table>
                <tbody>
                

















    
        <tr>
            <td>
                
                    Сведения отсутствуют
                
                    
            </td>
        </tr>
    
    

                </tbody>
            </table>
        </div>
    </div>
</div>
    </div>
  </div>
</div>
<script type="text/javascript">if (window.epzAnalytics) window.epzAnalytics.track();
$(document).ready(function () {
        checkNotice();
});
</script>



</body></html>'''
docs_html2 = '''<html><head>
  <meta http-equiv="content-type" content="text/html; charset=UTF-8">
  <link href="https://fonts.googleapis.com/css?family=Roboto+Slab:400,700&amp;subset=latin,cyrillic" rel="stylesheet" type="text/css">

  <title>Сведения закупки</title>

  <script type="text/javascript" async="" src="https://mc.yandex.ru/metrika/watch.js"></script><script type="text/javascript">
      var contextPath = "/epz/order/notice";
  </script>

  
    
    
      <link type="text/css" rel="stylesheet" media="all" href="/epz/order/notice/css/style.css">
      <link type="text/css" rel="stylesheet" href="/epz/order/notice/css/jquery_msgbox.css">
    
  

  <script type="text/javascript" src="/epz/order/notice/js/jquery-3.3.1.min.js"></script>
  <script type="text/javascript" src="/epz/order/notice/js/jquery.cookie.min.js"></script>
  <script type="text/javascript" src="/epz/order/notice/js/js.cookie.js"></script>
  <script type="text/javascript" src="/epz/order/notice/js/jquery_msgBox.js"></script>
  <script type="text/javascript">
      function sessionTimeOutMsg(){
          $.msgBox({
              type:"error",
              content:"Время ожидания соединения истекло",
              title: "Сообщение",
              afterClose: function(result) {
                  document.location.href = ""
              }
          });
      }
    
      var isRegisteredUserObozApp = Boolean("");
      var sessionMaxInactiveInterval = "";      
      $(document).ready(function(){
          var notUsual = (($.cookie("usePoorVisionOption") == 'true') && $(".goodVisionLink").length == 0);
          var notPoorVision = (($.cookie("usePoorVisionOption") != 'true') && $(".poorVisionLink").length == 0);
          if (notUsual || notPoorVision){
              location.reload();
          }
      });
  </script>
  <script>window.jQuery || document.write('<script src="/epz/order/notice/js/jquery-3.3.1.min.js"><\/script>')</script>
  <script type="text/javascript" src="/epz/order/notice/js/ui_autocomplete.js"></script>
  
  
  <script type="text/javascript" src="/epz/order/notice/js/mustache.min.js"></script>
  <script type="text/javascript" src="/epz/order/notice/js/jquery.price_format.1.7.js"></script>
  
  <script type="text/javascript" src="/epz/order/notice/js/moment.min.js"></script>
  <script type="text/javascript" src="/epz/order/notice/js/moment-timezone.min.js"></script>

  <script type="text/javascript" src="/epz/order/notice/js/action-switch.js"></script>
  <script type="text/javascript" src="/epz/order/notice/js/browser.js"></script>

  <script type="text/javascript" src="/epz/order/notice/js/script.js"></script>
  <script type="text/javascript" src="/epz/order/notice/js/cards_keyboard_control_script.js"></script>
  <script type="text/javascript" src="/epz/order/notice/js/custom.js"></script>
  <script type="text/javascript" src="/epz/order/notice/js/URI.js"></script>
  <script type="text/javascript" src="/epz/order/notice/js/common/config.js"></script>
  <script type="text/javascript" src="/epz/order/notice/js/common/analytics.js"></script>
  <script type="text/javascript" src="/epz/order/notice/js/cardBaseLayout.js"></script>
  
      
      
          <script type="text/javascript" src="/epz/order/notice/js/keyboardNavigationRules.js"></script>
      
  
  <script type="text/javascript" src="/epz/order/notice/js/keyboardControl.js"></script>
  <script type="text/javascript" src="/epz/order/notice/js/jquery-migrate-3.0.1.min.js"></script>
  <script type="text/javascript">
      var contextPath = "/epz/order/notice";
      var epzMainPublicUrl = "/epz/main/public/";
  </script>
  <script type="text/javascript" src="/epz/order/notice/js/checkNotice.js"></script>
  



<script type="text/javascript">
    epzCommonConfig.initCommonConfig({
        contextPath: '/epz/order/notice',
        smartSearchEnable: true,

        urls: {
            epzMainPublicUrl: '/epz/main/public/',
            epzNsiUrl: '/epz/nsi/',
            epzOrderUrl: '/epz/order/',
            epzOrderPlanUrl: '/epz/orderplan/',
            epzOrderClauseUrl: '/epz/orderclause/',
            epzContractUrl: '/epz/contract/',
            epzContractFz223Url: '/epz/contractfz223/',
            epzContractReportingUrl: '/epz/contractreporting/',
            epzCustomerReportsUrl: '/epz/customerreports/',
            epzOrganizationUrl: '/epz/organization/',
            epzDishonestSupplierUrl: '/epz/dishonestsupplier/',
            epzComplaintUrl: '/epz/complaint/',
            epzBankGuaranteeUrl: '/epz/bankguarantee/',
            epzInspectionPlanUrl: '/epz/inspectionplan/',
            epzUnscheduledInspectionUrl: '/epz/unscheduledinspection/',
            epzControlResultUrl: '/epz/controlresult/',
            epzDizkUrl: '/epz/dizk/',
            epzEsUrl: '/analytics/hit/',
            epzFarmUrl: '/epz/farm/'
        }
    });
</script>
  

<!-- Yandex.Metrika counter -->
<script type="text/javascript">
    (function (d, w, c) {
        (w[c] = w[c] || []).push(function() {
            try {
                w.yaCounter36706425 = new Ya.Metrika({
                    id:36706425,
                    clickmap:true,
                    trackLinks:true,
                    accurateTrackBounce:true
                });
            } catch(e) { }
        });

        var n = d.getElementsByTagName("script")[0],
                s = d.createElement("script"),
                f = function () { n.parentNode.insertBefore(s, n); };
        s.type = "text/javascript";
        s.async = true;
        s.src = "https://mc.yandex.ru/metrika/watch.js";

        if (w.opera == "[object Opera]") {
            d.addEventListener("DOMContentLoaded", f, false);
        } else { f(); }
    })(document, window, "yandex_metrika_callbacks");

    function yandexCounterHit(url) {
        if (typeof(yaCounter36706425) != "undefined") {
            yaCounter36706425.hit(url);
        }
    }

    $(document).ready(function () {
        $("a[target=_blank]:not([initialHref])").click(function (event) {
            yandexCounterHit($(this).attr("href"));
        });

        $(document).ajaxSend(function (event, request, settings) {
            yandexCounterHit(settings.url);
        });
    });

</script>
<noscript><div><img src="https://mc.yandex.ru/watch/36706425" style="position:absolute; left:-9999px;" alt="" /></div></noscript>
<!-- /Yandex.Metrika counter -->


</head>
<body class="cardLayout">

<script type="text/javascript">
  if ($.cookie('usePoorVisionOption') === 'true') {
    var body = $('body');
    var style = '';
    var cookie = $.cookie('colorSpectrumForPoorVision');
    if (cookie) {
      body.addClass(cookie + 'ColorSpectrum');
      switch (cookie) {
        case 'white':
          style = '#ffffff';
          break;
        case 'black':
          style = '#000000';
          break;
        case 'blue':
          style = '#9DD1FF';
          break;
        case 'brown':
          style = '#442713';
          break;
        case 'biege':
          style = '#F7F3D6';
          break;
        default:
          break;
      }
      body.css({backgroundColor: style});
    }

    var fontZize = $.cookie('fontSizeForPoorVision');
    if (fontZize) {
      body.addClass('fontSizeForPoorVision' + fontZize);
    }
  }
</script>

<div class="cardWrapper outerWrapper">

  <div class="wrapper">

    <div class="mainBox">
      






<script type="text/javascript">
    $(document).ready(function () {
        var poorVisionSettingsBlock = $('.poorVisionSettingsBlock');

        
        
        
        var poorVisionLink = poorVisionSettingsBlock.find('.poorVisionLink');

        poorVisionLink.click(function (e) {
            e.preventDefault();
            $.cookie('usePoorVisionOption', 'true', {path: '/', expires: 365*100});
            location.reload();
        });
        
        
    });

</script>

<div class="poorVisionSettingsBlock">
    
        
        
            <span>
                <a class="poorVisionLink poorVisionBannerCards"></a>
            </span>
        
    
</div>
      






















<div class="cardHeader">
    <a href="/epz/main/public/home.html" class="cardLogo"></a>
    <h1 class="padBtm8">Закупка №0262100002919000034
        <sup>
            
                
                
                    <a target="_blank" title="RSS-подписка на события закупки" href="/epz/order/notice/rss?regNumber=0262100002919000034">rss</a>
                
            
        </sup>
    </h1>

    
    <div class="public">
        
        Размещено: 31.01.2019 22:26 (MSK+2 (UTC+5) Екатеринбург) <br>По местному времени организации, осуществляющей закупку
    </div>
</div>


      



























<div class="contentTabs noticeTabs">
    <table class="contentTabsWrapper">
        <tbody><tr>
            













    <td tab="MAIN_INFO" parent="" url="/epz/order/notice/zk504/view/common-info.html?regNumber=0262100002919000034" class="">
        
            
            
            
                
            
        
        <div class="td-overflow"><span class="td-content"><span>Общая информация</span></span></div>
    </td>



            















            













    <td tab="PURCHASE_DOCS" parent="" url="/epz/order/notice/zk504/view/documents.html?regNumber=0262100002919000034" class="currentTab">
        
            
            
            
                
            
        
        <div class="td-overflow"><span class="td-content"><span>Документы закупки</span></span></div>
    </td>



            

            
                













    <td tab="SUPPLIER_RESULTS" parent="" url="/epz/order/notice/zk504/view/supplier-results.html?regNumber=0262100002919000034" class="">
        
            
            
            
                
            
        
        <div class="td-overflow"><span class="td-content"><span>Результаты определения поставщика</span></span></div>
    </td>


            

            













    <td tab="EVENT_LOG" parent="" url="/epz/order/notice/zk504/view/event-journal.html?regNumber=0262100002919000034" class="">
        
            
            
            
                
            
        
        <div class="td-overflow"><span class="td-content"><span>Журнал событий</span></span></div>
    </td>


        </tr>
    </tbody></table>
</div>


    <div class="padBtm20 contentHeadingWrapper" style="width: 620.641px;">
        
            <a target="_blank" class="size14" href="/epz/order/notice/printForm/view.html?printFormId=84861406">
                
                    
                        Извещение о проведении запроса котировок в электронной форме
                    
                    
                    
                
                от 31.01.2019 №0262100002919000034
            </a>
            <br>
        
    </div>


<script>
    $(document).ready(function () {
        $('.contentTabsWrapper td[tab = "PURCHASE_DOCS"]').addClass('currentTab');
        
            if ($('.contentTabsWrapper tr').width() > 980 && false) {
                $('[tab="EVENT_LOG"]').css('display', 'none');
            }
        
        
        
        
        
        
        
    });
</script>


      























<script type="text/javascript" src="/epz/order/notice/js/card/view/documentsButtonPanelNew.js"></script>

    
        <div class="padBtm20 revisionToggleWrapper">
            <div id="hide-editions">
                <span class="block-icon"></span>
                <a id="revisionViewToggle" href="javascript:toggleActiveRevisionView()">Отобразить недействующие
                    редакции</a>
            </div>
        </div>
    

<br class="clear">

<div class="contentTabBoxBlock">
    <div class="noticeTabBox padBtm20">
        <h2>Извещение, изменение извещения о проведении запроса котировок в электронной форме</h2>
        <div class="noticeTabBoxWrapper notice-documents padding-0-15px-15px-5px">
            <table>
                <tbody>
                

















    
    
        
        
            













    
    
        <tr class="  ">
            <td class="padRight5 width26px width165pxPV alignCenter">
                
                    <a class="linkPopUp pWidth_840 cryptoSigns" href="/epz/order/notice/signview/list.html?printFormId=84861406"></a>
                
            </td>
            
                <td class="width26px padLeft0 width165pxPV alignCenter">
                    <a class="printForm " href="/epz/order/notice/printForm/view.html?printFormId=84861406" title="Печатная форма" target="_blank"></a>
                </td>
            
            <td class="width_25_pr colorBlack  ">
                
                    
                    
                    
                        Извещение о проведении запроса котировок в электронной форме от 31.01.2019 №0262100002919000034
                    
                
            </td>
            <td class="width_35_pr ">
                
                    <div class="white-space-nowrap">
                        <span>Размещено</span>
                        <span class="white-space-nowrap padLeft10 floatRight">
                                    31.01.2019 22:26 <span class="timeZoneName" title="Екатеринбург">(МСК+2)</span>
                                </span>
                    </div>
                
                <span class="">
                                Действующая редакция
                                
                        </span>

                
            </td>
            <td class="width_30_pr ">
                
                    <div class=" cursorPointer" id="attachmentViewToggle" style="display: none;">
                        <span class="block-icon"></span>
                        <span class="empty">Показать все файлы</span>
                    </div>
                    
                        
                        <div class=" attachment">
                            <div class="white-space-nowrap floatLeft padRight5">
                                    <span class="vAlignMiddle margRight5 successCheckAntivirus" title="Проведена проверка на вирусы"></span>
                                
                                    <a class="linkPopUp pWidth_840 vAlignMiddle margRight5  cryptoSignsSmall" href="/epz/order/notice/signview/list.html?attachmentId=57816136">
                                    </a>
                                
                                <img alt="Microsoft Word Document" src="/epz/order/notice/images/icons/doc.png" class="vAlignMiddle margRight5" title="Microsoft Word Document">
                            </div>
                            <div class="displayTable">
                                <a class="" href="http://zakupki.gov.ru/44fz/filestore/public/1.0/download/priz/file.html?uid=6E2EA0327BE64A4DAE49301A8B5CB7C0" title="05-14 (2фил).doc">
                                        05-14 (2фил)
                                        </a>
                            </div>
                            <div class="clear"></div>
                        </div>
                    
                        
                        <div class=" attachment">
                            <div class="white-space-nowrap floatLeft padRight5">
                                    <span class="vAlignMiddle margRight5 successCheckAntivirus" title="Проведена проверка на вирусы"></span>
                                
                                    <a class="linkPopUp pWidth_840 vAlignMiddle margRight5  cryptoSignsSmall" href="/epz/order/notice/signview/list.html?attachmentId=57816137">
                                    </a>
                                
                                <img alt="Microsoft Word Document" src="/epz/order/notice/images/icons/doc.png" class="vAlignMiddle margRight5" title="Microsoft Word Document">
                            </div>
                            <div class="displayTable">
                                <a class="" href="http://zakupki.gov.ru/44fz/filestore/public/1.0/download/priz/file.html?uid=8F808B1041104EAEAC4EEF22F8D490FB" title="05-14 (2фил).doc">
                                        05-14 (2фил)
                                        </a>
                            </div>
                            <div class="clear"></div>
                        </div>
                    
                        
                        <div class=" attachment">
                            <div class="white-space-nowrap floatLeft padRight5">
                                    <span class="vAlignMiddle margRight5 successCheckAntivirus" title="Проведена проверка на вирусы"></span>
                                
                                    <a class="linkPopUp pWidth_840 vAlignMiddle margRight5  cryptoSignsSmall" href="/epz/order/notice/signview/list.html?attachmentId=57816138">
                                    </a>
                                
                                <img alt="Microsoft Word Document" src="/epz/order/notice/images/icons/doc.png" class="vAlignMiddle margRight5" title="Microsoft Word Document">
                            </div>
                            <div class="displayTable">
                                <a class="" href="http://zakupki.gov.ru/44fz/filestore/public/1.0/download/priz/file.html?uid=BBAAAF765DB74053AB50FC3BF4C83D9E" title="ПГК.docx">
                                        ПГК
                                        </a>
                            </div>
                            <div class="clear"></div>
                        </div>
                    
                
            </td>
        </tr>
    

            
                
                
                
                
                    
                    













    
    
        <tr class="  darkBackground">
            <td class="padRight5 width26px width165pxPV alignCenter">
                
                    <a class="linkPopUp pWidth_840 cryptoSigns" href="/epz/order/notice/signview/list.html?printFormId=84879906"></a>
                
            </td>
            
                <td class="width26px padLeft0 width165pxPV alignCenter">
                    <a class="printForm " href="/epz/order/notice/printForm/view.html?printFormId=84879906" title="Печатная форма" target="_blank"></a>
                </td>
            
            <td class="width_25_pr colorBlack  ">
                
                    
                        <a href="/epz/order/notice/printForm/view.html?printFormId=84879906" target="_blank">Уведомление о соответствии контролируемой информации</a>
                    
                    
                    
                
            </td>
            <td class="width_35_pr ">
                
                    <div class="white-space-nowrap">
                        <span>Размещено</span>
                        <span class="white-space-nowrap padLeft10 floatRight">
                                    31.01.2019 20:26
                                </span>
                    </div>
                
                <span class="">
                                
                                
                        </span>

                
            </td>
            <td class="width_30_pr ">
                
            </td>
        </tr>
    

                    
                
            
        
    

                </tbody>
            </table>
        </div>

        <h2>Изменение организации, осуществляющей размещение</h2>
        <div class="noticeTabBoxWrapper notice-documents padding-0-15px-15px-5px">
            <table>
                <tbody>
                

















    
        <tr>
            <td>
                
                    Сведения отсутствуют
                
                    
            </td>
        </tr>
    
    

                </tbody>
            </table>
        </div>

        <h2>Квитанции результатов согласования извещения на проведение запроса котировок в электронной форме</h2>
        <div class="noticeTabBoxWrapper notice-documents padding-0-15px-15px-5px">
            <table>
                <tbody>
                

















    
        <tr>
            <td>
                
                    Сведения отсутствуют
                
                    
            </td>
        </tr>
    
    

                </tbody>
            </table>
        </div>

        <h2>Отмена определения поставщика (подрядчика, исполнителя)</h2>
        <div class="noticeTabBoxWrapper notice-documents padding-0-15px-15px-5px">
            <table>
                <tbody>
                

















    
        <tr>
            <td>
                
                    Сведения отсутствуют
                
                    
            </td>
        </tr>
    
    

                </tbody>
            </table>
        </div>

        <h2>Протоколы работы комиссии, полученные с электронной площадки (ЭП)</h2>
        <div class="noticeTabBoxWrapper notice-documents padding-0-15px-15px-5px">
            <table>
                <tbody>
                












    
    
        
            
            <tr class=" ">
                <td class="width_30_pr colorBlack ">
                    
                        
                        
                            <a href="/epz/order/notice/zk504/view/protocol/protocol-main-info.html?regNumber=0262100002919000034&amp;protocolId=22201319">Протокол рассмотрения заявок на участие в запросе котировок в электронной форме от 12.02.2019 №ПР1</a>
                        
                        
                        
                    
                </td>
                <td class="width_30_pr">
                    
                        <div class="white-space-nowrap">
                            <span>Размещено на ЭП</span>
                            <span class="white-space-nowrap padLeft10">
                                12.02.2019 16:40 <span class="timeZoneName" title="Екатеринбург">(МСК+2)</span>
                            </span>
                        </div>
                    
                    
                    <div class="white-space-nowrap">
                        <span>Размещено в ЕИС</span>
                        <span class="white-space-nowrap padLeft10">
                            12.02.2019 16:40 <span class="timeZoneName" title="Екатеринбург">(МСК+2)</span>
                        </span>
                        
                    </div>
                    <span>Действующая редакция</span>
                </td>
                <td class="width_30_pr">
                    
                        <div class=" cursorPointer" id="attachmentViewToggle" style="display: none;">
                            <span class="block-icon"></span>
                            <span>Показать все файлы</span>
                        </div>
                        
                            
                            <div class=" attachment">
                                <div class="white-space-nowrap floatLeft padRight5">
                                    <span class="vAlignMiddle margRight5 successCheckAntivirus" title="Проведена проверка на вирусы"></span>
                                    
                                    <img alt="Текстовый документ" src="/epz/order/notice/images/icons/txt.png" class="vAlignMiddle margRight5" title="Текстовый документ">
                                </div>
                                <div class="displayTable">
                                    <a href="http://zakupki.gov.ru/44fz/filestore/public/1.0/download/priz/file.html?uid=3E99D2984A1E4D929B0AEF14B6590AC5" class="" title="Электронный документ, полученный из внешней системы.xml ()">
                                            Электронный документ
                                            ...
                                    </a>
                                </div>
                                <div style="clear:both"></div>
                            </div>
                        
                            
                            <div class=" attachment">
                                <div class="white-space-nowrap floatLeft padRight5">
                                    <span class="vAlignMiddle margRight5 successCheckAntivirus" title="Проведена проверка на вирусы"></span>
                                    
                                    <img alt="Microsoft Word Document" src="/epz/order/notice/images/icons/doc.png" class="vAlignMiddle margRight5" title="Microsoft Word Document">
                                </div>
                                <div class="displayTable">
                                    <a href="http://zakupki.gov.ru/44fz/filestore/public/1.0/download/priz/file.html?uid=A2DCB9DE97F44B8BB20779B919376A03" class="" title="Протокол_рассмотрения_заявок_на_участие_в_запросе_котировок(1_подана_1_соответствует)_(системный).docx ()">
                                            Протокол_рассмотрени
                                            ...
                                    </a>
                                </div>
                                <div style="clear:both"></div>
                            </div>
                        
                    
                </td>
            </tr>
        
            
            <tr class=" ">
                <td class="width_30_pr colorBlack ">
                    
                        
                        
                            <a href="/epz/order/notice/zk504/view/protocol/protocol-main-info.html?regNumber=0262100002919000034&amp;protocolId=22237745">Протокол рассмотрения и оценки заявок на участие в запросе котировок в электронной форме от 18.02.2019 №ПРО1</a>
                        
                        
                        
                    
                </td>
                <td class="width_30_pr">
                    
                        <div class="white-space-nowrap">
                            <span>Размещено на ЭП</span>
                            <span class="white-space-nowrap padLeft10">
                                18.02.2019 12:00 <span class="timeZoneName" title="Екатеринбург">(МСК+2)</span>
                            </span>
                        </div>
                    
                    
                    <div class="white-space-nowrap">
                        <span>Размещено в ЕИС</span>
                        <span class="white-space-nowrap padLeft10">
                            18.02.2019 12:01 <span class="timeZoneName" title="Екатеринбург">(МСК+2)</span>
                        </span>
                        
                    </div>
                    <span>Действующая редакция</span>
                </td>
                <td class="width_30_pr">
                    
                        <div class=" cursorPointer" id="attachmentViewToggle" style="display: none;">
                            <span class="block-icon"></span>
                            <span>Показать все файлы</span>
                        </div>
                        
                            
                            <div class=" attachment">
                                <div class="white-space-nowrap floatLeft padRight5">
                                    <span class="vAlignMiddle margRight5 successCheckAntivirus" title="Проведена проверка на вирусы"></span>
                                    
                                    <img alt="Текстовый документ" src="/epz/order/notice/images/icons/txt.png" class="vAlignMiddle margRight5" title="Текстовый документ">
                                </div>
                                <div class="displayTable">
                                    <a href="http://zakupki.gov.ru/44fz/filestore/public/1.0/download/priz/file.html?uid=03D053B21E164D21BF4C963EB3EF6B3A" class="" title="Электронный документ, полученный из внешней системы.xml ()">
                                            Электронный документ
                                            ...
                                    </a>
                                </div>
                                <div style="clear:both"></div>
                            </div>
                        
                            
                            <div class=" attachment">
                                <div class="white-space-nowrap floatLeft padRight5">
                                    <span class="vAlignMiddle margRight5 successCheckAntivirus" title="Проведена проверка на вирусы"></span>
                                    
                                    <img alt="Microsoft Word Document" src="/epz/order/notice/images/icons/doc.png" class="vAlignMiddle margRight5" title="Microsoft Word Document">
                                </div>
                                <div class="displayTable">
                                    <a href="http://zakupki.gov.ru/44fz/filestore/public/1.0/download/priz/file.html?uid=50310F07B59846FC95C2C682455F217C" class="" title="Протокол_рассмотрения_заявок_на_участие_в_запросе_котировок(1_подана_1_соответствует)_(системный).docx ()">
                                            Протокол_рассмотрени
                                            ...
                                    </a>
                                </div>
                                <div style="clear:both"></div>
                            </div>
                        
                    
                </td>
            </tr>
        
            
            <tr class=" ">
                <td class="width_30_pr colorBlack ">
                    
                        
                        
                            <a href="/epz/order/notice/zk504/view/protocol/protocol-main-info.html?regNumber=0262100002919000034&amp;protocolId=22328503">Протокол признания участника уклонившимся от заключения контракта от 26.02.2019 №ППУ1</a>
                        
                        
                        
                    
                </td>
                <td class="width_30_pr">
                    
                    
                    <div class="white-space-nowrap">
                        <span>Размещено в ЕИС</span>
                        <span class="white-space-nowrap padLeft10">
                            26.02.2019 16:34 <span class="timeZoneName" title="Екатеринбург">(МСК+2)</span>
                        </span>
                        
                    </div>
                    <span>Действующая редакция</span>
                </td>
                <td class="width_30_pr">
                    
                        <div class=" cursorPointer" id="attachmentViewToggle" style="display: none;">
                            <span class="block-icon"></span>
                            <span>Показать все файлы</span>
                        </div>
                        
                            
                            <div class=" attachment">
                                <div class="white-space-nowrap floatLeft padRight5">
                                    <span class="vAlignMiddle margRight5 successCheckAntivirus" title="Проведена проверка на вирусы"></span>
                                    
                                        <a class="linkPopUp pWidth_840 vAlignMiddle margRight5 cryptoSignsSmall" href="/epz/order/notice/signview/list.html?attachmentId=58730338"></a>
                                    
                                    <img alt="Adobe Acrobat Document" src="/epz/order/notice/images/icons/pdf.png" class="vAlignMiddle margRight5" title="Adobe Acrobat Document">
                                </div>
                                <div class="displayTable">
                                    <a href="http://zakupki.gov.ru/44fz/filestore/public/1.0/download/priz/file.html?uid=82C793BF011F0142E0530A86121F564F" class="" title="Протокол признания участника уклонившимся от заключения контракта.PDF ()">
                                            Протокол признания у
                                            ...
                                    </a>
                                </div>
                                <div style="clear:both"></div>
                            </div>
                        
                    
                </td>
            </tr>
        
    

                </tbody>
            </table>
        </div>

        <h2>Продление срока подачи заявок на участие в запросе котировок в электронной форме</h2>
        <div class="noticeTabBoxWrapper notice-documents padding-0-15px-15px-5px">
            <table>
                <tbody>
                

















    
    
        
        
            













    
    
        <tr class="  ">
            <td class="padRight5 width26px width165pxPV alignCenter">
                
                    <a class="linkPopUp pWidth_840 cryptoSigns" href="/epz/order/notice/signview/list.html?printFormId=85547294"></a>
                
            </td>
            
                <td class="width26px padLeft0 width165pxPV alignCenter">
                    <a class="printForm " href="/epz/order/notice/printForm/view.html?printFormId=85547294" title="Печатная форма" target="_blank"></a>
                </td>
            
            <td class="width_25_pr colorBlack  ">
                
                    
                    
                    
                        Извещение о продлении срока подачи заявок на участие в запросе котировок в электронной форме от 12.02.2019 №ИПС1
                    
                
            </td>
            <td class="width_35_pr ">
                
                    <div class="white-space-nowrap">
                        <span>Размещено</span>
                        <span class="white-space-nowrap padLeft10 floatRight">
                                    12.02.2019 16:50 <span class="timeZoneName" title="Екатеринбург">(МСК+2)</span>
                                </span>
                    </div>
                
                <span class="">
                                
                                
                        </span>

                
            </td>
            <td class="width_30_pr ">
                
            </td>
        </tr>
    

            
        
    

                </tbody>
            </table>
        </div>
    </div>
</div>
    </div>
  </div>
</div>
<script type="text/javascript">if (window.epzAnalytics) window.epzAnalytics.track();
$(document).ready(function () {
        checkNotice();
});
</script>



</body></html>'''
docs_html3 = '''<html><head>
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta http-equiv="content-type" content="text/html; charset=UTF-8">
    <meta name="description" content="Официальный сайт единой информационной системы в сфере закупок 44 ФЗ и 223 ФЗ">

    

    <title>Закупки</title>
    <script type="text/javascript" async="" src="https://mc.yandex.ru/metrika/watch.js"></script><script type="text/javascript">
        var contextPath = "/epz/order/quicksearch";
        var epzMainPublicUrl = "/epz/main/public/";
    </script>

    <link href="/epz/order/quicksearch/images/icons/Portal.ico" rel="shortcut icon">

    
        
        
            
            <link type="text/css" rel="stylesheet" media="all" href="/epz/order/quicksearch/css/app.css">
        
    

    <link type="text/css" rel="stylesheet" media="all" href="/epz/order/quicksearch/css/skin.css">
    <link type="text/css" rel="stylesheet" href="/epz/order/quicksearch/css/jquery.datepick.css">
    <link type="text/css" rel="stylesheet" href="/epz/order/quicksearch/css/barChart.css">
    <link type="text/css" rel="stylesheet" href="/epz/order/quicksearch/css/ui.dynatree.css">
    
        
        
            <link type="text/css" rel="stylesheet" href="/epz/order/quicksearch/css/jquery_msgbox.css">
        
    
    
    
    <script src="/epz/order/quicksearch/js/d3.v5.min.js"></script>
    <script src="/epz/order/quicksearch/js/jquery-3.3.1.min.js"></script>
    <script type="text/javascript" src="/epz/order/quicksearch/js/ui_autocomplete.js"></script>
    <script type="text/javascript" src="/epz/order/quicksearch/js/jquery-migrate-3.0.1.min.js"></script>
    <script type="text/javascript" src="/epz/order/quicksearch/js/validation/jquery.validate.js"></script>
    <script type="text/javascript" src="/epz/order/quicksearch/js/mustache.min.js"></script>
    <script type="text/javascript" src="/epz/order/quicksearch/js/jquery.price_format.1.7.js"></script>
    <script type="text/javascript" src="/epz/order/quicksearch/js/jquery.jcarousel.min.js"></script>
    <script type="text/javascript" src="/epz/order/quicksearch/js/jquery.maskedinput.min.js"></script>
    <script type="text/javascript" src="/epz/order/quicksearch/js/jquery.cookie.min.js"></script>
    <script type="text/javascript" src="/epz/order/quicksearch/js/js.cookie.js"></script>
    <script type="text/javascript">
        $(document).ready(function(){
            var notUsual = (($.cookie("usePoorVisionOption") == 'true') && $(".goodVisionLink").length == 0);
            var notPoorVision = (($.cookie("usePoorVisionOption") != 'true') && $(".poorVisionLink").length == 0);
            if (notUsual || notPoorVision){
                location.reload();
            }
        });
    </script>
    <script type="text/javascript" src="/epz/order/quicksearch/js/jquery.dynatree.js"></script>
    <script type="text/javascript" src="/epz/order/quicksearch/js/jquery.ui.datepicker-ru.js"></script>
    <script type="text/javascript" src="/epz/order/quicksearch/js/moment.min.js"></script>
    <script type="text/javascript" src="/epz/order/quicksearch/js/moment-timezone.min.js"></script>
    <script type="text/javascript" src="/epz/order/quicksearch/js/validation/jquery.numeric.js"></script>
    
    <script type="text/javascript" src="/epz/order/quicksearch/js/action-switch.js"></script>
    <script type="text/javascript" src="/epz/order/quicksearch/js/browser.js"></script>

    

    
        
        
            <script type="text/javascript" src="/epz/order/quicksearch/js/app.js"></script>
        
    

    

    <script type="text/javascript" src="/epz/order/quicksearch/js/baseLayout.js"></script>
    <script type="text/javascript" src="/epz/order/quicksearch/js/script.js"></script>
    <script type="text/javascript" src="/epz/order/quicksearch/js/checkNotice.js"></script>
    <script type="text/javascript" src="/epz/order/quicksearch/js/common/config.js"></script>
    <script type="text/javascript" src="/epz/order/quicksearch/js/common/choose-headagency.js"></script>
    <script type="text/javascript" src="/epz/order/quicksearch/js/common/choose-okpd.js"></script>
    <script type="text/javascript" src="/epz/order/quicksearch/js/custom.js"></script>
    <script type="text/javascript" src="/epz/order/quicksearch/js/popupCommon.js"></script>
    <script type="text/javascript" src="/epz/order/quicksearch/js/common/choose-organization.js"></script>
    <script type="text/javascript" src="/epz/order/quicksearch/js/URI.js"></script>
    <script type="text/javascript" src="/epz/order/quicksearch/js/common/analytics.js"></script>
    <script type="text/javascript" src="/epz/order/quicksearch/js/jquery_msgBox.js"></script>
    <script type="text/javascript" src="/epz/order/quicksearch/js/keyboardControl.js"></script>

    
        
        
            <script type="text/javascript" src="/epz/order/quicksearch/js/keyboardNavigationRules.js"></script>
        
    

    <script type="text/javascript">if (!window.console) console = {
        log: function () {
        }
    };</script>

    



<script type="text/javascript">
    epzCommonConfig.initCommonConfig({
        contextPath: '/epz/order/quicksearch',
        smartSearchEnable: true,

        urls: {
            epzMainPublicUrl: '/epz/main/public/',
            epzNsiUrl: '/epz/nsi/',
            epzOrderUrl: '/epz/order/',
            epzOrderPlanUrl: '/epz/orderplan/',
            epzOrderClauseUrl: '/epz/orderclause/',
            epzContractUrl: '/epz/contract/',
            epzContractFz223Url: '/epz/contractfz223/',
            epzContractReportingUrl: '/epz/contractreporting/',
            epzCustomerReportsUrl: '/epz/customerreports/',
            epzOrganizationUrl: '/epz/organization/',
            epzDishonestSupplierUrl: '/epz/dishonestsupplier/',
            epzComplaintUrl: '/epz/complaint/',
            epzBankGuaranteeUrl: '/epz/bankguarantee/',
            epzInspectionPlanUrl: '/epz/inspectionplan/',
            epzUnscheduledInspectionUrl: '/epz/unscheduledinspection/',
            epzControlResultUrl: '/epz/controlresult/',
            epzDizkUrl: '/epz/dizk/',
            epzEsUrl: '/analytics/hit/',
            epzFarmUrl: '/epz/farm/'
        }
    });
</script>
</head>
<body>

<script type="text/javascript">
    if ($.cookie('usePoorVisionOption') === 'true') {
        var body = $('body');
        var style = '', styleColor = '';
        var color = $.cookie('colorSpectrumForPoorVision');
        body.addClass('poorVision');
        if (color) {
            body.addClass(color + 'ColorSpectrum');
            switch (color) {
                case 'white':
                    style = '#ffffff';
                    styleColor = '#000000';
                    break;
                case 'black':
                    style = '#000000';
                    styleColor = '#ffffff'
                    break;
                case 'blue':
                    style = '#9DD1FF';
                    styleColor = '#063462';
                    break;
                case 'brown':
                    style = '#442713';
                    styleColor = '#a9e44d';
                    break;
                case 'biege':
                    style = '#F7F3D6';
                    styleColor = '#49442e';
                    break;
                default:
                    break;
            }
            body.css({backgroundColor: style, color:styleColor});
        }else{
            body.addClass('whiteColorSpectrum');
        }

        var fontSize = $.cookie('fontSizeForPoorVision');
        if (fontSize) {
            body.addClass('fontSizeForPoorVision' + fontSize);
        }else{
            body.addClass('fontSizeForPoorVision100');
        }
    }
</script>



    


    

    
    



























<div id="critical_notice"></div>

<header class="header header-top">
    <div class="container">
        <div class="row align-items-center">
            <div class="
            
                
                
                    col-2 offset-1
                
            
           " style="z-index: 1;">
                <span class="logo header-offset text-base-micro">Официальный сайт</span>
            </div>
            <div class="
            
                
                
                    col-3 offset-sm-2 offset-md-2 offset-lg-3
                
            
            ">
                <a id="chooseRegion" data-modalup="" href="/epz/nsi/kladr/chooseRegion.html">
                    <div class="region" data-toggle="modal-region" data-target=".modal-region">

                      <span class="region-city">
                        <span class="region-city__icon">
                          <img src="/epz/order/quicksearch/img/icons/icon_region.svg" title="Информация о местоположении пользователя используется в поисковых запросах для динамической детализации результатов поиска.">
                        </span>
                        <span class="region-city__text region-city__text_base text-base-micro">Мой регион: </span>
                      </span>
                        <span class="region-city">
                        <span class="region-city__text region-city__text_prime text-base-micro region_name" id="popUpUserRegionName">Не выбран</span>
                        <span class="region-city__icon">
                            <img src="/epz/order/quicksearch/img/icons/icon_arrow_region.svg" alt="">
                        </span>
                    </span>
                    </div>
                </a>
            </div>
            
                
                
                    <div class="col-1">
                        <div class="header-links-group offset-block">
                            <a href="#" class="header-link header-link_top">
                                <span class="header-link__icon poorVisionLink">
                                  <img class="glass-icon" src="/epz/order/quicksearch/img/icons/icon_eye.svg" alt="">
                                </span>
                            </a>
                        </div>
                    </div>
                
            
            <div class="
            
                
                
                 col-2
                
            
            ">
                <div class="account">
                    <div class="account-block">
                <span class="icon">
                  <img src="/epz/order/quicksearch/img/icons/icon_user.svg" alt="">
                </span>
                        <span class="text padLeft4">Личный кабинет</span>
                        <span class="button-open icon">
                  <img src="/epz/order/quicksearch/img/icons/icon_arrow_lk.svg" alt="">
                </span>
                    </div>
                    <ul class="account-vars" style="display: none;">
                        <li class="account__var" data-toggle="modal-account44">
                            <a class="account__link" data-modalup="" href="/epz/main/public/chooseAuth44.html" target="_blank">
                                <span class="icon">
                                  <img src="/epz/order/quicksearch/img/icons/arrow.svg" alt="">
                                </span>
                                <span class="text text_bottom">Личный кабинет</span>
                                <span class="subtext">44-Ф3</span>
                            </a>
                        </li>
                        <li class="account__var" data-toggle="modal-account223">
                            <a class="account__link" data-modalup="" href="/epz/main/public/chooseAuth223.html" target="_blank">
                                <span class="icon">
                                  <img src="/epz/order/quicksearch/img/icons/arrow.svg" alt="">
                                </span>
                                <span class="text text_bottom">Личный кабинет</span>
                                <span class="subtext">223-ФЗ</span>
                            </a>
                        </li>
                        <li class="account__var" data-toggle="modal-account-private">
                            <a href="http://eruz.zakupki.gov.ru/auth/welcome" class="account__link">
                                <span class="icon">
                                  <img src="/epz/order/quicksearch/img/icons/arrow.svg" alt="">
                                </span>
                                <span class="text text_bottom">Личный кабинет участника закупок</span>
                            </a>
                        </li>
                    </ul>
                </div>
            </div>
        </div>
    </div>
</header>
<header class="header header-mid">
    <div class="container">
        <div class="row">
            <div class="col-1">
                <a href="/epz/main/public/home.html">
                    <figure class="header-logo">
                        <img src="/epz/order/quicksearch/img/header/emblem.svg" class="header-logo__img" alt="">
                    </figure>
                </a>
            </div>
            <div class="col-4">
                <h3 id="header-title-site" onclick="location.href='/epz/main/public/home.html';" class="heading-h3 header-offset" title=""> Единая информационная система в&nbsp;сфере закупок</h3>
            </div>
            <div class="
            
                
                
                 col-3 offset-md-0 offset-lg-1
                
            
            ">
                <address class="phone">
                    <a href="tel:+74958110333" class="phone__text">
                        <span class="heading-h4">8 495 811-03-33</span>
                    </a>
                    <span class="phone__desc text-base-micro">Москва</span>
                </address>
                <address class="phone">
                    <a href="tel:+74958110333" class="phone__text">
                        <span class="heading-h4">8 800 333-81-11</span>
                    </a>
                    <span class="phone__desc text-base-micro">Россия</span>
                </address>
            </div>
            <div class="
            
                
                
                 col-3
                
            
            ">
                <div class="header-links-group offset-block">
                    <div class="wrapper-link">
                        <a href="/epz/main/public/user-feedback.html" class="header-link header-link header-link_icon_left">
                  <span class="header-link__icon">
                    <img src="/epz/order/quicksearch/img/icons/icon_mail.svg" alt="">
                  </span>
                            <span class="header-link__text header-link__text_prime">Техническая поддержка
                                
                            </span>
                        </a>
                    </div>
                    <div class="wrapper-link">
                        <a href="/epz/main/public/qa/view.html" class="header-link header-link header-link_icon_left">
                  <span class="header-link__icon">
                    <img src="/epz/order/quicksearch/img/icons/icon_quest.svg" alt="">
                  </span>
                            <span class="header-link__text header-link__text_prime">Часто задаваемые вопросы</span>
                        </a>
                    </div>
                </div>
            </div>
        </div>
    </div>
</header>

    
    
    

























<header class="header header-bottom">
    <div class="container">
        <div class="row">
            <div class="col-lg-12">
                <div class="menu-container">
                    <ul class="menu-mega" style="margin:0px;">
                        <ul class="menu-list">
                            
                            <li class="main-item hasnt-subitems" style="cursor: pointer; border-bottom: 3px solid rgb(0, 101, 221);">
                                <a href="/epz/order/quicksearch/search.html" class="_orderSearch main-link">Закупки</a>
                            </li>
                            <li class="main-item">
                                <a class="main-link">Планирование</a>
                                <ul>
                                    <li class="submenu-col">
                                        <ul class="submenu-list menu-list ">
                                            <li class="submenu-list__item">
                                                <a href="/epz/purchaseplanfz44/quicksearch/search.html" class="_purchasePlanFz44Search submenu-list__link">
                                                    <span class="link__text">Планы закупок</span>
                                                    <span class="link__desc">44-ФЗ</span>
                                                </a>
                                            </li>
                                            <li class="submenu-list__item">
                                                <a href="/epz/orderplan/quicksearch/search.html" class="_planSearch submenu-list__link">
                                                    <span class="link__text">Планы-графики закупок</span>
                                                    <span class="link__desc"> 44-ФЗ</span>
                                                    <span class="link__text"> и Планы закупки</span>
                                                    <span class="link__desc"> 223-ФЗ</span>
                                                </a>
                                            </li>
                                            <li class="submenu-list__item">
                                                <a href="/epz/oboz/public/quicksearch/search.html" class="_obozSearch submenu-list__link">
                                                    <span class="link__text">Обязательное общественное обсуждение закупок&nbsp;</span>
                                                    <span class="link__desc">44-ФЗ</span>
                                                </a>
                                            </li>
                                            <li class="submenu-list__item">
                                                <a href="/epz/pricereq/quicksearch/search.html" class="_pricereqSearch submenu-list__link">
                                                    <span class="link__text">Запросы цен товаров, работ, услуг</span>
                                                    <span class="link__desc">44-ФЗ</span>
                                                </a>
                                            </li>

                                            <li class="submenu-list__item">
                                                <a href="/epz/normalizationrules/quicksearch/search.html" class="_normalizationRulesSearch submenu-list__link">
                                                    <span class="link__text">Правила нормирования в сфере закупок</span>
                                                    <span class="link__desc">44-ФЗ</span>
                                                </a>
                                            </li>

                                            <li class="submenu-list__item">
                                                <a href="/epz/orderclause/quicksearch/search.html" class="_orderClauseSearch submenu-list__link">
                                                    <span class="link__text">Положения о закупке</span>
                                                    <span class="link__desc">223-ФЗ</span>
                                                </a>
                                            </li>

                                            <li class="submenu-list__item">
                                                <a href="/epz/typalclause/quicksearch/search.html" class="_typalClauseSearch submenu-list__link">
                                                    <span class="link__text">Типовые положения о закупке </span>
                                                    <span class="link__desc">223-ФЗ</span>
                                                </a>
                                            </li>

                                        </ul>
                                    </li>
                                </ul>
                            </li>
                            <li class="main-item">
                                <a class="main-link">Контракты и договоры</a>
                                <ul style="display: none; left: inherit;">
                                    <li class="submenu-col" style="width: 350px;">
                                        <ul class="submenu-list menu-list" style="display: none; left: inherit;">
                                            <li class="submenu-list__item" style="width: 350px;">
                                                <a href="/epz/contract/quicksearch/search.html" class="_contractSearch submenu-list__link">
                                                    <span class="link__text">Реестр контрактов</span>
                                                    <span class="link__desc">44-ФЗ</span>
                                                </a>
                                            </li>
                                            <li class="submenu-list__item" style="width: 350px;">
                                                <a href="/epz/contractfz223/quicksearch/search.html" class="_contractfz223 submenu-list__link">
                                                    <span class="link__text">Реестр договоров</span>
                                                    <span class="link__desc">223-ФЗ</span>
                                                </a>
                                            </li>

                                            <li class="submenu-list__item" style="width: 350px;">
                                                <a href="/epz/capitalrepairs/quicksearch/search.html" class="_capitalRepairsSearch submenu-list__link">
                                                    <span class="link__text">Реестр договоров о проведении капитального ремонта</span>
                                                    <span class="link__desc">ПП РФ 615</span>
                                                </a>
                                            </li>

                                            <li class="submenu-list__item" style="width: 350px;">
                                                <a href="/epz/dizk/quicksearch/search.html" class="_dizkSearch submenu-list__link">
                                                    <span class="link__text">Дополнительная информация о <br>контрактах</span>
                                                    <span class="link__desc">44-ФЗ</span>
                                                </a>
                                            </li>
                                            <li class="submenu-list__item" style="width: 350px;">
                                                <a href="/epz/btk/quicksearch/search.html" class="_btkSearch submenu-list__link">
                                                    <span class="link__text">Библиотека типовых контрактов, типовых условий контрактов</span>
                                                    <span class="link__desc">44-ФЗ</span>
                                                </a>
                                            </li>

                                        </ul>
                                    </li>
                                </ul>
                            </li>
                            <li class="main-item">
                                <a class="main-link">Организации</a>
                                <ul style="display: none; left: inherit;">
                                    <li class="submenu-col" style="width: 350px;">
                                        <ul class="submenu-list menu-list" style="display: none; left: inherit;">
                                            <li class="submenu-list__item" style="width: 350px;">
                                                <a href="/epz/organization/quicksearch/search.html" class="_organization_search submenu-list__link">
                                                    <span class="link__text">Реестр зарегистрированных организаций</span>
                                                    <span class="link__desc">44-ФЗ, 223-ФЗ</span>
                                                </a>
                                            </li>
                                            <li class="submenu-list__item" style="width: 350px;">
                                                <a href="/epz/customer223/quicksearch/search.html" class="_customer223Search submenu-list__link">
                                                    <span class="link__text">Реестр заказчиков</span>
                                                    <span class="link__desc">223-ФЗ</span>
                                                </a>
                                            </li>
                                            <li class="submenu-list__item" style="width: 350px;">
                                                <a href="/epz/eruz/quicksearch/search.html" class="_eruzSearch submenu-list__link">
                                                    <span class="link__text">Единый реестр участников закупок</span>
                                                    <span class="link__desc">44-ФЗ</span>
                                                </a>
                                            </li>

                                            <li class="submenu-list__item" style="width: 350px;">
                                                <a href="/epz/rkpo/quicksearch/search.html" class="_rkpoSearch submenu-list__link">
                                                    <span class="link__text">Сводный реестр квалифицированных подрядных организаций</span>
                                                    <span class="link__desc">ПП РФ 615</span>
                                                </a>
                                            </li>
                                        </ul>
                                    </li>
                                </ul>
                            </li>

                            <li class="main-item">
                                <a class="main-link">Мониторинг и отчетность</a>
                                <ul style="display: none; left: inherit;">
                                    <li class="submenu-col" style="width: 350px;">
                                        <ul class="submenu-list menu-list" style="display: none; left: inherit;">

                                            <li class="submenu-list__item" style="width: 350px;">
                                                <a href="/epz/legalacts/report/quicksearch/search.html" class="_freeAnalyticalReport submenu-list__link">
                                                    <span class="link__text">Сводные аналитические отчеты</span>
                                                    <span class="link__desc">44-ФЗ</span>
                                                </a>
                                            </li>
                                            <li class="submenu-list__item" style="width: 350px;">
                                                <a href="/epz/revenue/quicksearch/search.html" class="_revenueSearch submenu-list__link">
                                                    <span class="link__text">Реестр информации об объеме выручки отдельных видов юридических лиц</span>
                                                    <span class="link__desc">223-ФЗ</span>
                                                </a>
                                            </li>

                                            <li class="submenu-list__item" style="width: 350px;">
                                                <a href="/epz/customerreports/quicksearch/search.html?morphology=on&amp;pageNumber=1&amp;sortDirection=false&amp;recordsPerPage=_10&amp;sortBy=UPDATE_DATE&amp;fz44=on&amp;customerReportsType_0=on&amp;customerReportsType_1=on&amp;customerReportsType_2=on&amp;customerReportsType_3=on&amp;customerReportsType=0%2C1%2C2%2C3&amp;regionDeleted=false&amp;published=on" class="_customerReportsSearch44 submenu-list__link">
                                                    <span class="link__text">Отчеты заказчиков по контрактам</span>
                                                    <span class="link__desc">44-ФЗ</span>
                                                </a>
                                            </li>
                                        </ul>
                                        <ul class="containts_subitems" style="display: none; left: inherit;">
                                            <div style="width: 350px;">
                                                <li class="submenu-list__item__disabled">
                                                    <span class="submenu-list__link">
                                                        <span class="link__text">Отчеты заказчиков по договорам</span>
                                                        <span class="link__desc">223-ФЗ</span>
                                                    </span>
                                                </li>
                                            </div>

                                            <div class="submenu_subitem" style="width: 350px;">
                                                <li class="submenu-list__item ">
                                                    <a href="/epz/contractreporting/quicksearch/search.html" class="_contract-reporting submenu-list__link">
                                                        <span class="link__text">Сведения по договорам</span>
                                                    </a>
                                                </li>

                                                <li class="submenu-list__item">
                                                    <a href="/epz/customerreports/quicksearch/search.html?morphology=on&amp;pageNumber=1&amp;sortDirection=false&amp;recordsPerPage=_10&amp;sortBy=UPDATE_DATE&amp;fz223=on&amp;customerReportsType_4=on&amp;customerReportsType_5=on&amp;customerReportsType=4%2C5&amp;regionDeleted=false" class="_customerReportsSearch223 submenu-list__link">
                                                        <span class="link__text">Годовые отчеты</span>
                                                    </a>
                                                </li>
                                            </div>
                                        </ul>

                                        <ul style="display: none; left: inherit;">

                                            <li class="submenu-list__item" style="width: 350px;">
                                                <a href="/epz/activity/quicksearch/search.html" class="_activitySearch submenu-list__link">
                                                    <span class="link__text">Отчеты о проведенных контрольных мероприятиях в сфере закупок</span>
                                                    <span class="link__desc">44-ФЗ</span>
                                                </a>
                                            </li>
                                        </ul>
                                        <ul class="submenu-list menu-list" style="display: none; left: inherit;">
                                            <li class="submenu-list__item" style="width: 350px;">
                                                <a href="/epz/cmr/quicksearch/search.html" class="_cmrSearch submenu-list__link">
                                                    <span class="link__text">Отчет Корпорации МСП</span>
                                                    <span class="link__desc">223-ФЗ</span>
                                                </a>
                                            </li>
                                        </ul>

                                    </li>
                                </ul>
                            </li>

                            <li class="main-item">
                                <a class="main-link">Контроль и аудит</a>
                                <ul>
                                    <li class="submenu-col">
                                        <ul class="submenu-list menu-list">
                                            <li class="submenu-list__item">
                                                <a href="/epz/dishonestsupplier/quicksearch/search.html" class="_dishonestSupplierSearch submenu-list__link">
                                                    <span class="link__text">Реестр недобросовестных поставщиков (подрядчиков, исполнителей, подрядных организаций)
                                                        <span class="link__desc largeDecor">44-ФЗ, 223-ФЗ, ПП РФ 615</span>
                                                    </span>
                                                </a>
                                            </li>
                                        </ul>
                                        <ul class="containts_subitems">
                                            <div>
                                                <li class="submenu-list__item ">
                                                    <a href="/epz/main/public/aggregate-feedback.html" class="_aggregateFeedback submenu-list__link">
                                                        <span class="link__text">Реестр жалоб, плановых и внеплановых проверок, их результатов и выданных предписаний</span>
                                                        <span class="link__desc"></span>
                                                    </a>
                                                </li>
                                            </div>

                                            <div class="submenu_subitem">
                                                <li class="submenu-list__item ">
                                                    <a href="/epz/complaint/quicksearch/search_eis.html" class="_complaintSearch submenu-list__link">
                                                        <span class="link__text">Жалобы
                                                            <span class="link__desc">44-ФЗ, 223-ФЗ</span>
                                                        </span>
                                                    </a>
                                                </li>

                                                <li class="submenu-list__item">
                                                    <a href="/epz/inspectionplan/quicksearch/search_eis.html" class="_inspectionPlanSearch submenu-list__link">
                                                        <span class="link__text">Плановые проверки
                                                            <span class="link__desc">44-ФЗ</span>
                                                        </span>
                                                    </a>
                                                </li>

                                                <li class="submenu-list__item">
                                                    <a href="/epz/unscheduledinspection/quicksearch/search_eis.html" class="_unscheduledInspectionSearch submenu-list__link">
                                                        <span class="link__text">Внеплановые проверки
                                                            <span class="link__desc">44-ФЗ</span>
                                                        </span>
                                                    </a>
                                                </li>
                                                <li class="submenu-list__item">
                                                    <a href="/epz/controlresult/quicksearch/search_eis.html" class="_controlResultSearch submenu-list__link">
                                                        <span class="link__text">Результаты контроля
                                                            <span class="link__desc">44-ФЗ</span>
                                                        </span>
                                                    </a>
                                                </li>
                                            </div>
                                        </ul>

                                        <ul>
                                            <li class="submenu-list__item">
                                                <a href="/epz/audit/quicksearch/search.html" class="_auditSearch submenu-list__link">
                                                    <span class="link__text">Информация о результатах деятельности органов аудита
                                                        <span class="link__desc">44-ФЗ</span>
                                                    </span>
                                                </a>
                                            </li>
                                        </ul>

                                    </li>
                                </ul>
                            </li>

                            <li class="main-item">
                                <a class="main-link">Документы</a>
                                <ul class="submenu_with_threeblock" id="menu-columns-container-DOCUMENTS">
    <li class="submenu-col" id="menu-column-templateDOCUMENTS0">
    
    <ul class=" containts_subitems   ">
        <div>
            <li class="submenu-list__item">
                <a class="_1255 submenu-list__link" href="/epz/main/public/document/view.html?sectionId=1255">
                    <span class="link__text">Законодательство в сфере закупок
                        <span class="link__desc"></span>
                    </span>
                </a>
            </li>
        </div>
        <div class="submenu_subitem" id="menu-item-templateDOCUMENTS1255">

        
            <li class="submenu-list__item">
                <a class="_907 submenu-list__link" href="/epz/main/public/document/view.html?sectionId=907">
                    <span class="link__text">Нормативные правовые акты 44-ФЗ
                        <span class="link__desc"></span>
                    </span>
                </a>
            </li>

            <li class="submenu-list__item">
                <a class="_908 submenu-list__link" href="/epz/main/public/document/view.html?sectionId=908">
                    <span class="link__text">Нормативные правовые акты 223-ФЗ
                        <span class="link__desc"></span>
                    </span>
                </a>
            </li>

            <li class="submenu-list__item">
                <a class="_1261 submenu-list__link" href="/epz/main/public/document/view.html?sectionId=1261">
                    <span class="link__text">Национальный режим
                        <span class="link__desc"></span>
                    </span>
                </a>
            </li>

            <li class="submenu-list__item">
                <a class="_910 submenu-list__link" href="/epz/main/public/document/view.html?sectionId=910">
                    <span class="link__text">Разъяснения законодательства
                        <span class="link__desc"></span>
                    </span>
                </a>
            </li>
</div>
    </ul>

    <ul class=" containts_subitems   ">
        <div>
            <li class="submenu-list__item">
                <a class="_legalacts submenu-list__link" href="/epz/legalacts?sectionId=911">
                    <span class="link__text">Нормативно-методическая информация, предусмотренная для размещения в ЕИС
                        <span class="link__desc"></span>
                    </span>
                </a>
            </li>
        </div>
        <div class="submenu_subitem" id="menu-item-templateDOCUMENTS911">

        </div>
    </ul>

    <ul class=" containts_subitems   ">
        <div>
            <li class="submenu-list__item">
                <a class="_1252 submenu-list__link" href="/epz/main/public/document/view.html?sectionId=1252">
                    <span class="link__text">Техническая информация
                        <span class="link__desc"></span>
                    </span>
                </a>
            </li>
        </div>
        <div class="submenu_subitem" id="menu-item-templateDOCUMENTS1252">

        </div>
    </ul>

    <ul class=" containts_subitems   ">
        <div>
            <li class="submenu-list__item">
                <a class="_1254 submenu-list__link" href="/epz/main/public/document/view.html?sectionId=1254">
                    <span class="link__text">Сведения о банках и финансовых организациях
                        <span class="link__desc"></span>
                    </span>
                </a>
            </li>
        </div>
        <div class="submenu_subitem" id="menu-item-templateDOCUMENTS1254">

        </div>
    </ul>

    <ul class=" containts_subitems   ">
        <div>
            <li class="submenu-list__item">
                <a class="_1253 submenu-list__link" href="/epz/main/public/document/view.html?sectionId=1253">
                    <span class="link__text">Материалы для работы в ЕИС
                        <span class="link__desc"></span>
                    </span>
                </a>
            </li>
        </div>
        <div class="submenu_subitem" id="menu-item-templateDOCUMENTS1253">

        </div>
    </ul>
</li>
</ul>
                            </li>

                            <li class="main-item">
                                <a class="main-link">Дополнительная информация</a>
                                <ul class="submenu_with_threeblock" id="menu-columns-container-ADDITIONAL_INFO">
                                    <li class="submenu-col">
                                        <ul class="submenu-list menu-list">

                                            <li class="submenu-list__item">
                                                <a href="/epz/ktru/start/startPage.html" class="_ktruSearch submenu-list__link">
                                                    <span class="link__text">Каталог товаров, работ, услуг</span>
                                                    <span class="link__desc">44-ФЗ</span>
                                                </a>
                                            </li>

                                            <li class="submenu-list__item">
                                                <a href="/epz/bankguarantee/quicksearch/search.html" class="_bankGuaranteeSearch submenu-list__link">
                                                    <span class="link__text">Реестр банковских гарантий</span>
                                                    <span class="link__desc">44-ФЗ</span>
                                                </a>
                                            </li>
                                        </ul>

                                        <ul class="containts_subitems">

                                            <div>
                                                <li class="submenu-list__item__disabled ">
                                                    <span class="submenu-list__link">
                                                        <span class="link__text">Информация об инвестиционных контрактах</span>
                                                        <span class="link__desc">44-ФЗ</span>
                                                    </span>
                                                </li>
                                            </div>

                                            <div class="submenu_subitem">
                                                <li class="submenu-list__item ">
                                                    <a href="/epz/rep/quicksearch/search.html" class="_repSearch submenu-list__link">
                                                        <span class="link__text largeDecor">Реестр единственных поставщиков</span>
                                                        <span class="link__desc largeDecor">ст. 111.3, ст. 111.4 44-ФЗ</span>
                                                    </a>
                                                </li>

                                                <li class="submenu-list__item">
                                                    <a href="/epz/ropt/quicksearch/search.html" class="_roptSearch submenu-list__link">
                                                        <span class="link__text largeDecor">Отчеты производителей о соблюдении требований
                                                        <span class="link__desc largeDecor">п.5 ч.1 ст.111.3 44-ФЗ</span></span>
                                                    </a>
                                                </li>
                                            </div>
                                        </ul>
                                        <ul>
                                            <li class="submenu-list__item">
                                                <a href="/epz/gws/quicksearch/search.html" class="_gwsSearch submenu-list__link">
                                                    <span class="link__text">Перечни товаров, работ, услуг</span>
                                                    <span class="link__desc">223-ФЗ</span>
                                                </a>
                                            </li>
                                            <li class="submenu-list__item">
                                                <a href="/epz/mechproducts/quicksearch/search.html" class="_mechProducts submenu-list__link">
                                                    <span class="link__text">Перечни перспективных потребностей в продукции машиностроения </span>
                                                    <span class="link__desc">223-ФЗ</span>
                                                </a>
                                            </li>
                                        </ul>
                                    </li>
                                
    <li class="submenu-col" id="menu-column-templateADDITIONAL_INFO0">
    
    <ul class=" containts_subitems   ">
        <div>
            <li class="submenu-list__item">
                <a class="_915 submenu-list__link" href="/epz/main/public/document/view.html?sectionId=915">
                    <span class="link__text">Электронные площадки
                        <span class="link__desc"></span>
                    </span>
                </a>
            </li>
        </div>
        <div class="submenu_subitem" id="menu-item-templateADDITIONAL_INFO915">

        
            <li class="submenu-list__item">
                <a class="_index.html submenu-list__link" href="/epz/etp/list/index.html?sectionId=916">
                    <span class="link__text">Перечень отобранных операторов электронных площадок
                        <span class="link__desc"></span>
                    </span>
                </a>
            </li>

            <li class="submenu-list__item">
                <a class="_917 submenu-list__link" href="/epz/main/public/document/view.html?sectionId=917">
                    <span class="link__text">Тарифы электронных площадок
                        <span class="link__desc"></span>
                    </span>
                </a>
            </li>
</div>
    </ul>

    <ul class="  submenu-list menu-list  ">
            <li class="submenu-list__item">
                <a class="_918 submenu-list__link" href="/epz/main/public/document/view.html?sectionId=918">
                    <span class="link__text">Единый агрегатор торговли
                        <span class="link__desc"></span>
                    </span>
                </a>
            </li>
    </ul>

    <ul class="  submenu-list menu-list  ">
            <li class="submenu-list__item">
                <a class="_opendata submenu-list__link" href="/epz/opendata?sectionId=919">
                    <span class="link__text">Открытые данные
                        <span class="link__desc"></span>
                    </span>
                </a>
            </li>
    </ul>

    <ul class="  submenu-list menu-list  ">
            <li class="submenu-list__item">
                <a class="_920 submenu-list__link" href="/epz/main/public/document/view.html?sectionId=920">
                    <span class="link__text">Независимый регистратор
                        <span class="link__desc"></span>
                    </span>
                </a>
            </li>
    </ul>

    <ul class=" containts_subitems   ">
        <div>
            <li class="submenu-list__item">
                <a class="_921 submenu-list__link" href="/epz/main/public/document/view.html?sectionId=921">
                    <span class="link__text">Архив
                        <span class="link__desc"></span>
                    </span>
                </a>
            </li>
        </div>
        <div class="submenu_subitem" id="menu-item-templateADDITIONAL_INFO921">

        </div>
    </ul>
</li>
</ul>
                            </li>
                        </ul>
                    </ul>
                </div>
            </div>
        </div>
    </div>
</header>

<script type="text/javascript">
    function selectCurrentMenuItem() {
        
        var sectionSelector = "li:has(a[class*='_orderSearch'])";

        if ($(sectionSelector).attr('class') == $('.hasnt-subitems').attr('class'))
            
            
        
        $(sectionSelector).css('border-bottom', '3px solid #0065dd');
        
        
    else
        {
            
            
            
            $(sectionSelector).parents('ul').parents('li').not($(this).parents('ul')).last().css('border-bottom', '3px solid #0065dd');
            
            
            if ($('._orderSearch').parent() != 'li')
                $('._orderSearch').parent('li').addClass('active-subitems');
        }
        
    }

    $(document).ready(function () {
        selectCurrentMenuItem();
    });
</script>
    

    
    
    
    



















<script type="text/javascript" src="/epz/order/quicksearch/js/search/quickSearch.js"></script>
<script type="text/javascript" src="/epz/order/quicksearch/js/search/saveQuickSearchSettingsPopup.js"></script>
<script type="text/javascript" src="/epz/order/quicksearch/js/search/search.js"></script>
<script type="text/javascript" src="/epz/order/quicksearch/js/quickSearchForm.js"></script>
<script type="text/javascript" src="/epz/order/quicksearch/js/jquery.ui.datepicker.validation.js"></script>
<script type="text/javascript" src="/epz/order/quicksearch/js/validation/jqueryCustomValidateFields.js"></script>




<form id="quickSearchForm_header" action="/epz/order/quicksearch/search.html" method="GET" class="formValidation" novalidate="novalidate">

    
        
    




















<script type="text/javascript" src="/epz/order/quicksearch/js/searchString.js"></script>

    



    
    
        <div class="searchBlockAll zakupkiSearch">
            <div class="searchBox  titleTop">
                
                    <span class="titleField padBtm5 ">Закупки</span>
                        
                    
                    
                

                <div class="searchField">
                    <input type="text" id="searchString" class="autocompleteOrder hint clearValue 
                               withoutAutocomplete" name="searchString" value="Введите полностью или часть номера, наименования закупки, идентификационного кода закупки (ИКЗ), наименования или ИНН Заказчика" title="Введите полностью или часть номера, наименования закупки, идентификационного кода закупки (ИКЗ), наименования или ИНН Заказчика" autocomplete="off" style="color: rgb(153, 153, 153);">

                    <div class="clearButton" style="visibility: hidden;"></div>
                    <input type="button" value="" onclick="submitQuickSearchForm();">
                </div>
                <p class="accounting">
                    
                        
                        
                            
                                
                                
                                    <a href="#" onclick="goExtendedSearch('/epz/order/extendedsearch/search.html')" class="extendedSearchLink floatRight">Расширенный поиск</a>
                                
                            
                        
                        
                    

                    <label>
                <span id="morphologyWrapper" class="customCheck
                 
                        
                             check
                        
                        
                    " onclick="morphologyWrapperClick()">
                    <input type="checkbox" id="morphology" name="morphology" checked="checked" class="margLeft1" onclick="uncheckSearchStringCheckBox($('#strictEqual'));">
                </span>
                        С учетом всех форм слов
                    </label>

                    <label>
                <span id="strictEqualWrapper" class="mainPageStrictEqual customCheck " onclick="strictEqualWrapperClick()">
                    <input type="checkbox" id="strictEqual" name="strictEqual" class="margLeft3" onclick="uncheckSearchStringCheckBox($('#morphology'));" value="false">
                </span>
                        Строгое соответствие
                    </label>
                </p>
            </div>
        </div>
    


    

    

    

    <div class="filterParametrs">
        <div class="collapceBox collapceAdd"><span class="collapce">Свернуть фильтр</span><span class="expand d-none">Развернуть фильтр</span>
        </div>
        <ul>

            
                
                
                    <li class="currentPar" id="setParametersTitle">Установленные параметры</li>

                
            

            <li class="currentPar" id="editParametersTitle" style="display: none;">Уточняющие параметры</li>
            <li onclick="showSearchParameters()" id="setParametersLink" class="withoutBorder">
                <a href="#">Уточнить параметры поиска</a>
            </li>
            
        </ul>
        <div class="clear"></div>
    </div>

    <div class="filterBlock">
        
            <div class="greyBox pseudoInputBox margBtm10">
                <div class="tuningQuickSearchBlock">
                    <div class="pseudoInput greyText">Выбрать сохраненную настройку поиска</div>
                    <div id="savedSettingBox" class="tuningQuickSearchBox">
                        <ul class="tuningQuickSearchList">
                            <li>
                                <span data-redirect="http://zakupki.gov.ru/epz/order/quicksearch/search.html" class="tuningQuickSearchTitle greyText">Выбрать сохраненную настройку поиска</span>
                            </li>
                            <li id="savedSettingPrototype" style="display: none;">
                                <span class="tuningQuickSearchToolBox"><span class="editingBtn"></span><span class="delBtn"></span></span>
                                <span data-redirect="" class="tuningQuickSearchTitle"></span>
                            </li>
                        </ul>
                    </div>
                </div>
            </div>
        

        <div class="greyBox">
            <ul class="listParametrsSearch" id="searchOptionsViewContainer">
                
                    
                
                    
                        
                        
                        
                        
                        





















<li id="orderPlaceOfSearchViewTag">
    
        
            <label>Закупки по:</label>
        
        
    
    
        <span class="resultItem" data-input="fz44">44-ФЗ<span style="display: inline-block;height: 18px;"></span></span>
        





    
    
        <span class="resultItem" data-input="fz223">223-ФЗ<span style="display: inline-block;height: 18px;"></span></span>
        





    
    
    
</li>

                    
                
                    
                        
                        
                        
                        
                        













































                    
                
                    
                        
                        
                        
                        
                        


























    <li><label>Этап закупки:</label>
    
        
        
            
                <span class="resultItem" data-input="af">Подача заявок<span></span></span>
                





            
            
                <span class="resultItem" data-input="ca">Работа комиссии<span></span></span>
                





            
            
                <span class="resultItem" data-input="pc">Процедура завершена<span></span></span>
                





            
            
                <span class="resultItem" data-input="pa">Процедура отменена<span></span></span>
                





            
            </li>
        
    


                    
                
                    
                        
                        
                        
                        
                        





















    <li>
        
            
            

                
                

                
                    
                    
                        
                            
                            
                            
                                
                                
                                
                            
                        
                    
                

                
            
        
        
        





        





        
            





        
    </li>

                    
                
                    
                        
                        
                        
                        
                        



























                    
                
                    
                        
                        
                        
                        
                        
























                    
                
                    
                        
                        
                        
                        
                        



















                    
                
                    
                        
                        
                        
                        
                        
































                    
                
                    
                        
                        
                        
                        
                        




















                    
                
                    
                        
                        
                        
                        
                        




















                    
                
                    
                        
                        
                        
                        
                        




















                    
                
                    
                

                <li class="clear"></li>
            </ul>

            <ul class="listParametrsChoice reestrQuaranty" id="searchOptionsEditContainer">
                

                    
                    
                    
                    



















<script type="text/javascript">
    $(document).ready(function () {
        $("#showLotsInfoHidden").prop("checked", false);
        $("#expandLotsInfo").prop("checked", false);
        expandLots($("#expandLotsInfo"));
    });
</script>

<input type="hidden" id="pageNumber" name="pageNumber" value="1">
<input type="hidden" name="sortDirection" value="false">
<input type="hidden" name="recordsPerPage" value="_10">
<input type="hidden" id="showLotsInfoHidden" name="showLotsInfoHidden" value="false">

                

                    
                    
                    
                    
























<script type="text/javascript">
    $(document).ready(function () {
        $("#placeOfSearchTag").on("setDefaultValues", function () {
            $("#fz44").prop("checked", true);
            $("#fz223").prop("checked", true);
            $("#fz94").prop("checked", false);
            
                $("#ppRf615").prop("checked", false);
            
            _placeOfSearchDispatchEvent(false);
        });

        $("#placeOfSearchTag input[type='checkbox']").on("delete", function (event) {
            $(this).prop("checked", false);
            _placeOfSearchDispatchEvent(false);
        });

        _placeOfSearchDispatchEvent(true);
    });

    function _placeOfSearchDispatchEvent(isInit) {
        var checkedList = $("#placeOfSearchTag input[type='checkbox']:checked");
        var placeOfSearchList = $.map(checkedList, function (item) {
            return $(item).attr("data-placeOfSearch");
        });
        $('#searchOptionsEditContainer').children('.placeOfSearchEventListener').each(function () {
            $(this).trigger("placeOfSearchEvent", {
                placeOfSearchList: placeOfSearchList,
                isInitEvent: isInit
            });
        });
        var classesList = "";
        if (placeOfSearchList.indexOf('FZ_223') != -1 && placeOfSearchList.length == 1) {
            if ($("#LOTS").is(":checked")) {
                classesList = ".fz223_l_tag";
            } else {
                classesList = ".fz223_tag";
            }
        } else {
            $.each(checkedList, function (i, item) {
                classesList = classesList + $(item).attr("data-className");
            });
        }
        epzCommonChooseOrganization.setListPlaceOfSearch(placeOfSearchList);
        _changeTagsVisibility(classesList ? classesList : ".fz44_tag.fz223_tag.fz94_tag.ppRf615_tag");
    }
    function _placeOfSearchDispatchEventLaw(isInit) {
        _placeOfSearchDispatchEvent(isInit);
        
        var organizationNames = "agency".split(",");
        if(organizationNames !== undefined && organizationNames.length > 0) {
            $.each(organizationNames, function (key, value) {
                epzCommonChooseOrganization.clearOrganizationFields(value.trim());
            });
        }
        
    }
</script>
<li id="placeOfSearchTag" class="">
    
        
            <label>Закупки по:</label>
        
        
    
    <ul class="lowList">
        <li class="customCheckbox">
            <input type="checkbox" onchange="_placeOfSearchDispatchEventLaw(false)" checked="" id="fz44" name="fz44" data-classname=".fz44_tag" data-placeofsearch="FZ_44">
            <label for="fz44">44-ФЗ
            </label>
        </li>
        <li class="customCheckbox">
            <input type="checkbox" onchange="_placeOfSearchDispatchEventLaw(false)" checked="" id="fz223" name="fz223" data-classname=".fz223_tag" data-placeofsearch="FZ_223">
            <label for="fz223">223-ФЗ
                <span class="help margLeft10" title="Доступен выбор типа поиска по атрибутам закупок или по атрибутам лотов"></span>
            </label>
        </li>
        
            <li class="customCheckbox">
                <input type="checkbox" onchange="_placeOfSearchDispatchEventLaw(false)" id="ppRf615" name="ppRf615" data-classname=".ppRf615_tag" data-placeofsearch="PP_RF_615">
                <label for="ppRf615"> ПП РФ 615 (Капитальный ремонт)
                </label>
            </li>
        
        <li class="customCheckbox">
            <input type="checkbox" onchange="_placeOfSearchDispatchEventLaw(false)" id="fz94" name="fz94" data-classname=".fz94_tag" data-placeofsearch="FZ_94">
            <label for="fz94">94-ФЗ
            </label>
        </li>
    </ul>
</li>


                

                    
                    
                    
                    

<script src="/epz/order/quicksearch/js/search/includes/edit/subway.js"></script>

























<div style="display: none;" id="customPurchaseMethodTemplate">
    <ul>
        <li class="placingWay223Item">
            <label>
                <input type="checkbox" class="show_FZ_223" checked="checked" id="">
            </label>
            <span class="delBtn margRight5 floatRight"></span>
        </li>
    </ul>
</div>

<li id="placingWaysTag" class="placeOfSearchEventListener padBtm1 ">
    <label class="vAlignTop padTop8">
        
            
            
                Способ определения поставщика, подрядной организации<br>
                <span class="greyText">(размещения закупки)</span>:
            
        
    </label>

    <div class="manySelect width630 margBtm5 inlineBlock">

        <div class="collapsed height30">
            <span class="msExpandButton"></span>
            <span data-initial="Выберите одно или несколько значений" class="msPlaceholder" title="Выберите одно или несколько значений">Выберите одно или несколько значений</span>
        </div>
        <div class="selectChose">
            <div class="expanded">
                <ul class="placingWayList" id="placingWayList">
<li class="customCheckbox show_FZ_44" placingway_id="FZ_44_OK504">
        <input type="checkbox" id="placingWay_FZ_44_OK504" data-code="FZ_44_OK504" class="show_FZ_44">
        <label style="width: calc(100% - 50px);" for="placingWay_FZ_44_OK504">Открытый конкурс в электронной форме
        </label>
    </li>

<li class="customCheckbox show_FZ_44" placingway_id="FZ_44_ZK504">
        <input type="checkbox" id="placingWay_FZ_44_ZK504" data-code="FZ_44_ZK504" class="show_FZ_44">
        <label style="width: calc(100% - 50px);" for="placingWay_FZ_44_ZK504">Запрос котировок в электронной форме
        </label>
    </li>

<li class="customCheckbox show_FZ_44" placingway_id="FZ_44_ZP504">
        <input type="checkbox" id="placingWay_FZ_44_ZP504" data-code="FZ_44_ZP504" class="show_FZ_44">
        <label style="width: calc(100% - 50px);" for="placingWay_FZ_44_ZP504">Запрос предложений в электронной форме
        </label>
    </li>

<li class="customCheckbox show_FZ_44" placingway_id="FZ_44_OKU504">
        <input type="checkbox" id="placingWay_FZ_44_OKU504" data-code="FZ_44_OKU504" class="show_FZ_44">
        <label style="width: calc(100% - 50px);" for="placingWay_FZ_44_OKU504">Конкурс с ограниченным участием в электронной форме
        </label>
    </li>

<li class="customCheckbox show_FZ_44" placingway_id="FZ_44_OKD504">
        <input type="checkbox" id="placingWay_FZ_44_OKD504" data-code="FZ_44_OKD504" class="show_FZ_44">
        <label style="width: calc(100% - 50px);" for="placingWay_FZ_44_OKD504">Двухэтапный конкурс в электронной форме
        </label>
    </li>

<li class="customCheckbox show_FZ_223" placingway_id="FZ_223_KESMBO">
        <input type="checkbox" id="placingWay_FZ_223_KESMBO" data-code="FZ_223_KESMBO" class="show_FZ_223">
        <label style="width: calc(100% - 50px);" for="placingWay_FZ_223_KESMBO">Конкурс в электронной форме, участниками которого могут являться только субъекты малого и среднего предпринимательства
        </label>
    </li>

<li class="customCheckbox show_FZ_223" placingway_id="FZ_223_AESMBO">
        <input type="checkbox" id="placingWay_FZ_223_AESMBO" data-code="FZ_223_AESMBO" class="show_FZ_223">
        <label style="width: calc(100% - 50px);" for="placingWay_FZ_223_AESMBO">Аукцион в электронной форме, участниками которого могут являться только субъекты малого и среднего предпринимательства
        </label>
    </li>

<li class="customCheckbox show_FZ_223" placingway_id="FZ_223_ZKESMBO">
        <input type="checkbox" id="placingWay_FZ_223_ZKESMBO" data-code="FZ_223_ZKESMBO" class="show_FZ_223">
        <label style="width: calc(100% - 50px);" for="placingWay_FZ_223_ZKESMBO">Запрос котировок в электронной форме, участниками которого могут являться только субъекты малого и среднего предпринимательства
        </label>
    </li>

<li class="customCheckbox show_FZ_223" placingway_id="FZ_223_ZPESMBO">
        <input type="checkbox" id="placingWay_FZ_223_ZPESMBO" data-code="FZ_223_ZPESMBO" class="show_FZ_223">
        <label style="width: calc(100% - 50px);" for="placingWay_FZ_223_ZPESMBO">Запрос предложений в электронной форме, участниками которого могут являться только субъекты малого и среднего предпринимательства
        </label>
    </li>

<li class="customCheckbox show_FZ_94" placingway_id="FZ_94_EF" style="display: none;">
        <input type="checkbox" id="placingWay_FZ_94_EF" data-code="FZ_94_EF" class="show_FZ_94">
        <label style="width: calc(100% - 50px);" for="placingWay_FZ_94_EF">Открытый аукцион в электронной форме
        </label>
    </li>

<li class="customCheckbox show_FZ_94" placingway_id="FZ_94_SZ" style="display: none;">
        <input type="checkbox" id="placingWay_FZ_94_SZ" data-code="FZ_94_SZ" class="show_FZ_94">
        <label style="width: calc(100% - 50px);" for="placingWay_FZ_94_SZ">Сообщение о заинтересованности в проведении открытого конкурса
        </label>
    </li>

<li class="customCheckbox show_FZ_44" placingway_id="FZ_44_ZKB44">
        <input type="checkbox" id="placingWay_FZ_44_ZKB44" data-code="FZ_44_ZKB44" class="show_FZ_44">
        <label style="width: calc(100% - 50px);" for="placingWay_FZ_44_ZKB44">Запрос котировок без размещения извещения
        </label>
    </li>

<li class="customCheckbox show_FZ_94" placingway_id="FZ_94_ZH" style="display: none;">
        <input type="checkbox" id="placingWay_FZ_94_ZH" data-code="FZ_94_ZH" class="show_FZ_94">
        <label style="width: calc(100% - 50px);" for="placingWay_FZ_94_ZH">Результат рассмотрения и оценки котировочных заявок (Глава 5 Федерального закона №94-Ф3)
        </label>
    </li>

<li class="customCheckbox show_FZ_94" placingway_id="FZ_94_TB" style="display: none;">
        <input type="checkbox" id="placingWay_FZ_94_TB" data-code="FZ_94_TB" class="show_FZ_94">
        <label style="width: calc(100% - 50px);" for="placingWay_FZ_94_TB">Торги на товарных биржах
        </label>
    </li>

<li class="customCheckbox show_FZ_44" placingway_id="FZ_44_OKD44">
        <input type="checkbox" id="placingWay_FZ_44_OKD44" data-code="FZ_44_OKD44" class="show_FZ_44">
        <label style="width: calc(100% - 50px);" for="placingWay_FZ_44_OKD44">Двухэтапный конкурс
        </label>
    </li>

<li class="customCheckbox show_FZ_44" placingway_id="FZ_44_INM111">
        <input type="checkbox" id="placingWay_FZ_44_INM111" data-code="FZ_44_INM111" class="show_FZ_44">
        <label style="width: calc(100% - 50px);" for="placingWay_FZ_44_INM111">Способ определения поставщика (подрядчика, исполнителя), установленный Правительством Российской Федерации в соответствии со ст. 111 Федерального закона № 44-ФЗ
        </label>
    </li>

<li class="customCheckbox show_FZ_94 show_FZ_44 show_FZ_223" placingway_id="FZ_94_OK,FZ_44_OK44,FZ_223_OK">
        <input type="checkbox" id="placingWay_FZ_94_OKFZ_44_OK44FZ_223_OK" data-code="FZ_94_OK,FZ_44_OK44,FZ_223_OK" class="show_FZ_94 show_FZ_44 show_FZ_223">
        <label style="width: calc(100% - 50px);" for="placingWay_FZ_94_OKFZ_44_OK44FZ_223_OK">Открытый конкурс
        </label>
    </li>

<li class="customCheckbox show_FZ_44" placingway_id="FZ_44_ZP44">
        <input type="checkbox" id="placingWay_FZ_44_ZP44" data-code="FZ_44_ZP44" class="show_FZ_44">
        <label style="width: calc(100% - 50px);" for="placingWay_FZ_44_ZP44">Запрос предложений
        </label>
    </li>

<li class="customCheckbox show_FZ_94 show_FZ_44 show_FZ_223" placingway_id="FZ_94_ZK,FZ_44_ZK44,FZ_223_ZK">
        <input type="checkbox" id="placingWay_FZ_94_ZKFZ_44_ZK44FZ_223_ZK" data-code="FZ_94_ZK,FZ_44_ZK44,FZ_223_ZK" class="show_FZ_94 show_FZ_44 show_FZ_223">
        <label style="width: calc(100% - 50px);" for="placingWay_FZ_94_ZKFZ_44_ZK44FZ_223_ZK">Запрос котировок
        </label>
    </li>

<li class="customCheckbox show_PP_RF_615" placingway_id="PP_RF_615_PO615" style="display: none;">
        <input type="checkbox" id="placingWay_PP_RF_615_PO615" data-code="PP_RF_615_PO615" class="show_PP_RF_615">
        <label style="width: calc(100% - 50px);" for="placingWay_PP_RF_615_PO615">Предварительный отбор квалифицированных подрядных организаций
        </label>
    </li>

<li class="customCheckbox show_FZ_44" placingway_id="FZ_44_OKU44">
        <input type="checkbox" id="placingWay_FZ_44_OKU44" data-code="FZ_44_OKU44" class="show_FZ_44">
        <label style="width: calc(100% - 50px);" for="placingWay_FZ_44_OKU44">Конкурс с ограниченным участием
        </label>
    </li>

<li class="customCheckbox show_FZ_44 show_FZ_223" placingway_id="FZ_44_EP44,FZ_223_EP">
        <input type="checkbox" id="placingWay_FZ_44_EP44FZ_223_EP" data-code="FZ_44_EP44,FZ_223_EP" class="show_FZ_44 show_FZ_223">
        <label style="width: calc(100% - 50px);" for="placingWay_FZ_44_EP44FZ_223_EP">Закупка у единственного поставщика (подрядчика, исполнителя)
        </label>
    </li>

<li class="customCheckbox show_FZ_44" placingway_id="FZ_44_ZKK44">
        <input type="checkbox" id="placingWay_FZ_44_ZKK44" data-code="FZ_44_ZKK44" class="show_FZ_44">
        <label style="width: calc(100% - 50px);" for="placingWay_FZ_44_ZKK44">Закрытый конкурс
        </label>
    </li>

<li class="customCheckbox show_PP_RF_615" placingway_id="PP_RF_615_EA615" style="display: none;">
        <input type="checkbox" id="placingWay_PP_RF_615_EA615" data-code="PP_RF_615_EA615" class="show_PP_RF_615">
        <label style="width: calc(100% - 50px);" for="placingWay_PP_RF_615_EA615">Электронный аукцион на оказание услуг или выполнение работ по капитальному ремонту общего имущества в многоквартирном доме
        </label>
    </li>

<li class="customCheckbox show_FZ_94 show_FZ_223" placingway_id="FZ_94_OA,FZ_223_OA">
        <input type="checkbox" id="placingWay_FZ_94_OAFZ_223_OA" data-code="FZ_94_OA,FZ_223_OA" class="show_FZ_94 show_FZ_223">
        <label style="width: calc(100% - 50px);" for="placingWay_FZ_94_OAFZ_223_OA">Открытый аукцион
        </label>
    </li>

<li class="customCheckbox show_FZ_94" placingway_id="FZ_94_ES" style="display: none;">
        <input type="checkbox" id="placingWay_FZ_94_ES" data-code="FZ_94_ES" class="show_FZ_94">
        <label style="width: calc(100% - 50px);" for="placingWay_FZ_94_ES">Единственный поставщик
        </label>
    </li>

<li class="customCheckbox show_FZ_44" placingway_id="FZ_44_ZKKU44">
        <input type="checkbox" id="placingWay_FZ_44_ZKKU44" data-code="FZ_44_ZKKU44" class="show_FZ_44">
        <label style="width: calc(100% - 50px);" for="placingWay_FZ_44_ZKKU44">Закрытый конкурс с ограниченным участием
        </label>
    </li>

<li class="customCheckbox show_FZ_44 show_FZ_223" placingway_id="FZ_44_EA44,FZ_223_EF">
        <input type="checkbox" id="placingWay_FZ_44_EA44FZ_223_EF" data-code="FZ_44_EA44,FZ_223_EF" class="show_FZ_44 show_FZ_223">
        <label style="width: calc(100% - 50px);" for="placingWay_FZ_44_EA44FZ_223_EF">Электронный аукцион
        </label>
    </li>

<li class="customCheckbox show_FZ_94 show_FZ_44" placingway_id="FZ_94_PO,FZ_44_PO44">
        <input type="checkbox" id="placingWay_FZ_94_POFZ_44_PO44" data-code="FZ_94_PO,FZ_44_PO44" class="show_FZ_94 show_FZ_44">
        <label style="width: calc(100% - 50px);" for="placingWay_FZ_94_POFZ_44_PO44">Предварительный отбор
        </label>
    </li>

<li class="customCheckbox show_FZ_44" placingway_id="FZ_44_ZKKD44">
        <input type="checkbox" id="placingWay_FZ_44_ZKKD44" data-code="FZ_44_ZKKD44" class="show_FZ_44">
        <label style="width: calc(100% - 50px);" for="placingWay_FZ_44_ZKKD44">Закрытый двухэтапный конкурс
        </label>
    </li>

<li class="customCheckbox show_FZ_44" placingway_id="FZ_44_ZA44">
        <input type="checkbox" id="placingWay_FZ_44_ZA44" data-code="FZ_44_ZA44" class="show_FZ_44">
        <label style="width: calc(100% - 50px);" for="placingWay_FZ_44_ZA44">Закрытый аукцион
        </label>
    </li>

<li class="customCheckbox show_FZ_223" placingway_id="FZ_223_PR">
        <input type="checkbox" id="placingWay_FZ_223_PR" data-code="FZ_223_PR" class="show_FZ_223">
        <label style="width: calc(100% - 50px);" for="placingWay_FZ_223_PR">Прочее
        </label>
    </li>
</ul>
            </div>
            <div id="placingWaysSelectBtnDiv" class="msButtonIn">
                <span id="placingWaysSelectBtn" class="btnBtn blueBtn">Выбрать</span>

                <a id="223CustomWaysAddLink" href="/epz/order/quicksearch/purchase/open.html" class="btnBtn blueBtn linkPopUp margLeft5" style="display: none;"><span class="addBtn">Добавить</span></a>
            </div>

            
        </div>
    </div>
    <input type="hidden" id="placingWaysList" name="placingWaysList" value="">
    <input type="hidden" id="placingWaysList223" name="placingWaysList223" value="">
</li>

<script type="text/javascript">
    $(document).ready(function () {
        $(".listParametrsChoice input[type='checkbox']").on("delete", function () {
            _removeCheckVal($(this));
        });

        $(document).on( 'click', '.placingWay223Item > span', function(){
            $(this).parent().remove();
        });

        document.getElementById('223CustomWaysAddLink').addEventListener( 'click', function(){
            var placingWay223ItemCount = $('.placingWay223Item').length-1;
            if(placingWay223ItemCount > 9){
                $(this).prop('href', '');
            }else{
                $(this).prop('href', '/epz/order/quicksearch/purchase/open.html');
            }
        });

        $("#placingWaysTag").on("setDefaultValues", function () {
            $("div.selectChose :checkbox").prop("checked", false);
            $("#placingWaysTag .msPlaceholder").text("Выберите одно или несколько значений").removeClass("choseColor");
            $("#placingWayList .placingWay223Item").remove();
            $("#placingWaysList").val("");
            $("#placingWaysList223").val("");
        }).on("placeOfSearchEvent", function (e, data) {
            var placeOfSearchList = data.placeOfSearchList;
            if (placeOfSearchList.join().search("FZ_223") != -1 && placeOfSearchList.length == 1) {
                $("#223CustomWaysAddLink").show();
            } else {
                $("#223CustomWaysAddLink").hide();
            }

            if (placeOfSearchList.join().search("FZ_44") != -1 && placeOfSearchList.length == 1) {
                $("#inm111").show();
            } else {
                $("#inm111").hide();
            }

            var rowsSelectors = [];
            $.each(data.placeOfSearchList, function (index, valueCss) {
                rowsSelectors.push("li.show_" + valueCss);
            });
            var allRows = $("#placingWaysTag li");
            var needRows = $("#placingWaysTag " + rowsSelectors.join(","));
            $.each(needRows, function (index, value) {
                $(value).toggle(true);
            });

            var hideRows = [];
            jQuery.grep(allRows, function (el) {
                if (jQuery.inArray(el, needRows) == -1) hideRows.push(el);
            });

            $.each(hideRows, function (index, value) {
                $(value).find(":checkbox").prop('checked', false);
                $(value).toggle(false);
            });
            initHiddens();
            setManySelectPlaceholderText("placingWaysSelectBtnDiv");
        });
        _placeOfSearchDispatchEvent(false);
        setManySelectPlaceholderText("placingWaysSelectBtnDiv");

        $("#placingWaysSelectBtn").click(function () {
            initHiddens();
        });

        
        _placeOfSearchDispatchEvent(true);
        

        initHiddens();

        setPlacingWayPRCheckHandler();

        setPlacingWay223ItemCheckHandler();
    });

    // дублировано из placeOfSearch. в contract223 placeOfSearch.jsp отсутствует.
    

    function _placeOfSearchDispatchEvent(isInit) {
        var checkedList = $("#placeOfSearchTag input[type='checkbox']:checked");
        var placeOfSearchList = $.map(checkedList, function (item) {
            return $(item).attr("data-placeOfSearch");
        });
        $('#placingWaysTag').each(function () {
            $(this).trigger("placeOfSearchEvent", {
                placeOfSearchList: placeOfSearchList,
                isInitEvent: isInit
            });
        });
        var classesList = "";
        if (placeOfSearchList.indexOf('FZ_223') != -1 && placeOfSearchList.length == 1) {
            if ($("#LOTS").is(":checked")) {
                classesList = ".fz223_l_tag";
            } else {
                classesList = ".fz223_tag";
            }
        } else {
            $.each(checkedList, function (i, item) {
                classesList = classesList + $(item).attr("data-className");
            });
        }
        _changeTagsVisibility(classesList ? classesList : ".fz44_tag.fz223_tag.fz94_tag.ppRf615_tag");
    }

    

    function get_purchase_methods() {
        return $("#placingWayList").find("li label input:checked");
    }
    ;

    function insert_purchase_methods(selKeys) {
        var PLACINGWAYPRCHECK = $("#placingWay_FZ_223_PR");
        $(selKeys).each(function (i, el) {
            var checkElementExists = $("#placingWay223_" + el.id);
            if(!checkElementExists.length){
                var newElem = $("#customPurchaseMethodTemplate ul li").clone(true);
                $("input[type='checkbox']", newElem).attr("id", "placingWay223_" + el.id);
                $("label", newElem).append(el.name);
                uncheckSearchStringCheckBox(PLACINGWAYPRCHECK);
                $("#placingWayList").append(newElem);
            }else{
                checkElementExists.prop("checked", true);
            }
        });

    }
    ;


    function setPlacingWayPRCheckHandler() {
        var PLACINGWAYPRCHECK = $("#placingWay_FZ_223_PR");
        PLACINGWAYPRCHECK.change(function (e) {
            if ($(this).is(":checked")) {
                uncheckSearchStringCheckBox($("#placingWayList li.placingWay223Item input:checked"));
            }
        });
    }

    function setPlacingWay223ItemCheckHandler() {
        var PLACINGWAYPRCHECK = $("#placingWay_FZ_223_PR");
        $("#placingWaysTag").on("change", "li.placingWay223Item input[type='checkbox']", function (e) {
            if ($(this).is(":checked")) {
                uncheckSearchStringCheckBox(PLACINGWAYPRCHECK);
            }
        });
    }

    function initHiddens() {
        setPlacingWaysHiddenValue($("input[id^=placingWay_]:checked"), $("#placingWaysList"), 11, "placingWay");
        setHiddenValue($("input[id^=placingWay223_]:checked"), $("#placingWaysList223"), 14);
        $('#searchOptionsEditContainer').children('.placingWaysEventListener').each(function () {
            $(this).trigger("placingWaysEvent", {
                placingWays44: $("#placingWaysList").val()
            });
        });
    }
    ;
</script>






















<li id="placingChildWaysTag" class="placeOfSearchEventListener padBtm1 " style="display: none;">
    <label class="vAlignTop padTop8">
        
            
            
                Предусмотрены особенности осуществления закупки
            
        
    </label>

    <div class="manySelect width630 margBtm5 inlineBlock">

        <div class="collapsed height30">
            <span class="msExpandButton"></span>
            <span data-initial="Выберите одно или несколько значений" class="msPlaceholder" title="Выберите одно или несколько значений">Выберите одно или несколько значений</span>
        </div>
        <div id="choiceContainer" class="selectChose">
            <div class="expanded">
                <ul class="placingWayList" id="childrenWayList">
                    
                </ul>
            </div>
            <div id="childWaysSelectBtnDiv" class="msButtonIn">
                <span id="childWaysSelectBtn" class="btnBtn blueBtn">Выбрать</span>
            </div>
        </div>
    </div>
    <input type="hidden" id="placingChildWaysList" name="placingChildWaysList" value="">
</li>

<script type="text/javascript">
    $(document).ready(function () {
        initArgs({
            ulBlockId: '#childrenWayList',
            templateId: '#childWayTemplateId',
            hiddenInputId: '#placingChildWaysList',
            choiceContainerId: '#choiceContainer',
            selectButtonId: '#childWaysSelectBtn',
            tagId: '#placingChildWaysTag',
            childSelector: 'placingWay',
            hint: 'Выберите одно или несколько значений',
            btnContainer: 'childWaysSelectBtnDiv',
            templatesPath:'/epz/order/quicksearch/js/templates/placingWayItemTemplate.htm'
        });

        changeVisibleSubWays();
    });

    function changeVisibleSubWays() {
        var vals = "";
        var tag = $('#placingChildWaysTag');
        var selectedWayToDefineSupplier = "[]";
        if (vals.length > 0 || (selectedWayToDefineSupplier.length > 0 && $("#fz44").is(":checked") && $("#placeOfSearchTag").find("input[type='checkbox']:checked").length == 1)) {
            $(tag).show();
        } else {
            $(tag).hide();
        }
    }
</script>
<script type="text/javascript">
    $(document).ready(function () {
        var mapping = window.location.protocol + "//" + window.location.host + "/epz/nsi/placingway/parents.json";

        function init(data) {
            $.get(templatesPath, function (templates) {
                $("#placingWayList").empty();
                var wayElem = $(templates).filter("#childWayTemplateId").html();
                for (var index in data) {
                    var item = data[index];
                    var laws = "";
                    var codes = "";
                    var ident = "";
                    for (var i in item.laws) {
                        var lawItem = item.laws[i];
                        laws += (i > 0 ? " " : "") + "show_" + lawItem.fzName;
                        codes += (i > 0 ? "," : "") + lawItem.fzIdentifier;
                        ident += lawItem.fzIdentifier;
                    }
                    var dataItems = {
                        code: codes,
                        title: item.title,
                        law: laws,
                        ident: ident
                    };
                    $("#placingWayList").append(Mustache.render(wayElem, dataItems));
                }

                
                _placeOfSearchDispatchEvent(true);
                setPlacingWayPRCheckHandler();
            });

            if ($("#fz44").is(":checked")) {
                $("#inm111").show();
            }

            $("#placingWayList input[type='checkbox']").on("delete", function () {
                _removeCheckVal($(this));
                initHiddens();
            });

            $("#placingWaysTag").on("placeOfSearchEvent", function (e, data) {
                var placeOfSearchList = data.placeOfSearchList;
                if (placeOfSearchList.join().search("FZ_223") != -1 && placeOfSearchList.length == 1) {
                    $("#223CustomWaysAddLink").show();
                } else {
                    $("#223CustomWaysAddLink").hide();
                }

                if (placeOfSearchList.join().search("FZ_44") != -1) {
                    $("#inm111").show();
                } else {
                    $("#inm111").hide();
                }

                var rowsSelectors = [];
                $.each(data.placeOfSearchList, function (index, valueCss) {
                    rowsSelectors.push("li.show_" + valueCss);
                });
                var allRows = $("#placingWaysTag li");
                var needRows = $("#placingWaysTag " + rowsSelectors.join(","));
                $.each(needRows, function (index, value) {
                    $(value).toggle(true);
                });

                var hideRows = [];
                jQuery.grep(allRows, function (el) {
                    if (jQuery.inArray(el, needRows) == -1) hideRows.push(el);
                });

                $.each(hideRows, function (index, value) {
                    $(value).find(":checkbox").prop('checked', false);
                    $(value).toggle(false);
                });
                initHiddens();
                setManySelectPlaceholderText("placingWaysSelectBtnDiv");
            });
            $("#placingWaysSelectBtn").click(function () {
                initHiddens();
                initChildren($("input[id^=placingWay_]:checked"));
            });
        }

            $.ajax({
                url: mapping,
                success: function (data) {
                    init(data);
                }
            });
    });

</script>

                

                    
                    
                    
                    
























<script type="text/javascript">
    $(document).ready(function () {
        $("#orderStages").on("setDefaultValues", function () {
            $("#af").prop("checked", true);
            $("#ca").prop("checked", true);
            $("#pc").prop("checked", true);
            $("#pa").prop("checked", true);
            setManySelectPlaceholderText("orderStagesSelectBtn");
        });
        setManySelectPlaceholderText("orderStagesSelectBtn");

        $("#orderStages input[type='checkbox']").on("delete", function (event) {
            $(this).prop("checked", false);
        });
    });

</script>
<li id="orderStages" class=""><label>Этап закупки:</label>

    <div class="manySelect width630 inlineBlock verticalMiddle">
        <div class="collapsed height30">
            <span class="msExpandButton"></span>
            <span data-initial="Выберите одно или несколько значений" title="" class="msPlaceholder choseColor">
                        
                        Подача заявок
                        
                    , 
                        
                        Работа комиссии
                        
                    , 
                        
                        Процедура завершена
                        
                    , 
                        
                        Процедура отменена
                        
                    </span>
        </div>
        <div class="selectChose">
            <div class="expanded">
                <ul>
                    <li class="customCheckbox">
                        <input type="checkbox" checked="" id="af" name="af">
                        <label for="af">Подача заявок
                        </label>
                    </li>
                    <li class="customCheckbox">
                        <input type="checkbox" checked="" id="ca" name="ca">
                        <label for="ca">Работа комиссии
                        </label>
                    </li>
                    <li class="customCheckbox">
                        <input type="checkbox" checked="" id="pc" name="pc">
                        <label style="width: calc(100% - 50px);" for="pc">Процедура завершена
                        </label>
                    </li>
                    <li class="customCheckbox">
                        <input type="checkbox" checked="" id="pa" name="pa">
                        <label style="width: calc(100% - 50px);" for="pa">Процедура отменена
                        </label>
                    </li>
                </ul>
            </div>
            <div id="orderStagesSelectBtn" class="msButtonIn"><span class="btnBtn blueBtn">Выбрать</span></div>
        </div>
    </div>
</li>


                

                    
                    
                    
                    






















    
    
        
    

<script type="text/javascript">
    $(document).ready(function () {
        $("#orderQuickContractPrice").on("setDefaultValues", function () {
            $("#priceFrom").prop("value", "Минимальная цена");
            $("#priceTo").prop("value", "Максимальная цена");
            $("#currencyId").val("-1").change();
            $('#currencyChangecurrencyId').html("Любая").addClass("greyText");
        });

        $("#orderQuickContractPrice input[type='text']").on("delete", function (event) {
            
            
            
            $("#orderQuickContractPrice input[type='text']").val("");
            
            
        });
        $("#orderQuickContractPrice #currencyChangecurrencyId").on("delete", function (event) {
            $(this).html("Любая");
            $("#currencyId").val("-1");
        });
        $("span.tuningQuickSearchTitle.currencyChangecurrencyId").click(function () {
            $("#currencyId").val(this.id);
            if (this.id == '-1') {
                $('#currencyChangecurrencyId').addClass("greyText");
            } else {
                $('#currencyChangecurrencyId').removeClass("greyText");
            }
        });
        $('#currencyChangecurrencyId').click(function () {
            $("#contextSearchcurrencyId").focus();
        });

        $("#setParametersLink").on("click", function () {
            if (false) {
                if (true) {
                    $("#priceFrom").prop("value", "0");
                }
                if (true) {
                    $("#priceTo").prop("value", "200000000000");
                }
            }
        });
        if (false) {
            if (true) {
                $("#priceFrom").prop("value", "0");
            }
            if (true) {
                $("#priceTo").prop("value", "200000000000");
            }
        }
        if ($("#currencyId").val() == "-1") {
            $('#currencyChangecurrencyId').addClass("greyText")
        }

        $(".currencyElement").on("show", function () {
            $(this).find("#hideCurrencycurrencyId").val(0);
        });

        $(".currencyElement").on("hide", function () {
            $(this).find("#hideCurrencycurrencyId").val(1);
        });
        var currencies = $("#hideCurrencycurrencyId").closest(".currencyElement");
        var showCurrency = currencies.length > 0 && currencies.css("display") !== "none";
        $("#hideCurrencycurrencyId").val(showCurrency ? 0 : 1);
    });
</script>

<li id="orderQuickContractPrice" class="">

    <label>Начальная (максимальная) цена контракта (договора):
    </label>
    <span class=" padRight5">от</span>
    <input type="text" class=" size110 height30 margRight10 numeric  hint width160 " id="priceFrom" name="priceFrom" maxlength="20" title="Минимальная цена" value="" data-default_value="Минимальная цена" style="color: rgb(153, 153, 153);">
    <span class="padRight5">до</span>
    <input type="text" class=" margRight10 size110 height30 numeric  hint width160 " id="priceTo" name="priceTo" title="Максимальная цена" value="" maxlength="20" data-validate="{&quot;required&quot;: &quot;false&quot;, &quot;compareNumbers&quot;: &quot;#priceFrom&quot;,&quot;checkNumbers&quot;: &quot;#priceFrom&quot;}" data-validate_message="{&quot;compareNumbers&quot;: &quot;Минимальная сумма не может быть больше максимальной&quot;,
                                   &quot;checkNumbers&quot;:&quot;Цены указаны неверно&quot;}" data-default_value="Максимальная цена" data-validate-number-range="" style="color: rgb(153, 153, 153);">
    
    
        
    

    <div class="currencyLabel padTop5 ">
        <label>Валюта:</label>
        
            <div class="tuningQuickSearchBlock inlineBlock vAlignMiddle height30 width-245-px ">
                <div class="pseudoSelect greyText" id="currencyChangecurrencyId">
                    
                        
                            Любая
                        
                        
                    
                </div>
                <div class="tuningQuickSearchBox">
                    <ul class="tuningQuickSearchList">
                        <li>
                        <span>
                            <input id="contextSearchcurrencyId">
                        </span>
                        </li>
                        <li>
                            <span class="tuningQuickSearchTitle currencyChangecurrencyId grayText currencyChange" id="-1">
                            Любая
                            </span>
                        </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="1">
                                    Российский рубль
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="3">
                                    Доллар США
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="2">
                                    Евро
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="8767656">
                                    %
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324885">
                                    Австралийский доллар
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6325021">
                                    Азербайджанский манат
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324883">
                                    Алжирский динар
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324884">
                                    Аргентинское песо
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324889">
                                    Армянский драм
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324967">
                                    Арубанский флорин
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324870">
                                    Афгани
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324886">
                                    Багамский доллар
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324974">
                                    Бальбоа
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324890">
                                    Барбадосский доллар
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324995">
                                    Бат
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324887">
                                    Бахрейнский динар
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324895">
                                    Белизский доллар
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="9146353">
                                    Белорусский рубль
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324873">
                                    Белорусский рубль
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324891">
                                    Бермудский доллар
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324874">
                                    Болгарский лев
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6325016">
                                    Боливар
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="25483431">
                                    Боливар Соберано
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324893">
                                    Боливиано
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324881">
                                    Бразильский реал
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324897">
                                    Брунейский доллар
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324899">
                                    Бурундийский франк
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324968">
                                    Вату
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324943">
                                    Вона
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6325025">
                                    Восточно-карибский доллар
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324926">
                                    Гайанский доллар
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6325015">
                                    Ганский седи
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324925">
                                    Гвинейский франк
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324923">
                                    Гибралтарский фунт
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324929">
                                    Гонконгский доллар
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324878">
                                    Гривна
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324976">
                                    Гуарани
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324927">
                                    Гурд
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324922">
                                    Даласи
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324913">
                                    Датская крона
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6325001">
                                    Денар
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324998">
                                    Дирхам (ОАЭ)
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324983">
                                    Добра
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="21890270">
                                    Добра
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6325013">
                                    Доллар Зимбабве
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324964">
                                    Доллар Намибии
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324903">
                                    Доллар Островов Кайман
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324896">
                                    Доллар Соломоновых Островов
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324997">
                                    Доллар Тринидада и Тобаго
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324920">
                                    Доллар Фиджи
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324914">
                                    Доминиканское песо
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324988">
                                    Донг
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6325002">
                                    Египетский фунт
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324869">
                                    Единица реальной стоимости
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6325010">
                                    Замбийская квача
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="8265974">
                                    Замбийская квача
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324880">
                                    Злотый
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324970">
                                    Золотая кордоба
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324938">
                                    Иена
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324932">
                                    Индийская рупия
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324940">
                                    Иорданский динар
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324935">
                                    Иракский динар
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324934">
                                    Иранский риал
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324931">
                                    Исландская крона
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6325009">
                                    Йеменский риал
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324901">
                                    Канадский доллар
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324979">
                                    Катарский риал
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324872">
                                    Кванза
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324941">
                                    Кенийский шиллинг
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324924">
                                    Кетсаль
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324975">
                                    Кина
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324907">
                                    Колумбийское песо
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324908">
                                    Коморский франк
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324876">
                                    Конвертируемая марка
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6325012">
                                    Конвертируемое песо
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324875">
                                    Конголезский франк
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324909">
                                    Коста-риканский колон
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324918">
                                    Крона
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324911">
                                    Кубинское песо
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324944">
                                    Кувейтский динар
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324910">
                                    Куна
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324898">
                                    Кьят
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324946">
                                    Лаосский кип
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324879">
                                    Лари
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324949">
                                    Латвийский лат
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324882">
                                    Лек
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324928">
                                    Лемпира
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324986">
                                    Леоне
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324950">
                                    Либерийский доллар
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324947">
                                    Ливанский фунт
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324951">
                                    Ливийский динар
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324991">
                                    Лилангени
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324952">
                                    Литовский лит
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324948">
                                    Лоти
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324958">
                                    Маврикийская рупия
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324954">
                                    Малавийская квача
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324868">
                                    Малагасийский ариари
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324955">
                                    Малайзийский ринггит
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324962">
                                    Марокканский дирхам
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324959">
                                    Мексиканское песо
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6325020">
                                    Мозамбикский метикал
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324961">
                                    Молдавский лей
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324971">
                                    Найра
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324917">
                                    Накфа
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324892">
                                    Нгултрум
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324965">
                                    Непальская рупия
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324966">
                                    Нидерландский антильский гульден
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324969">
                                    Новозеландский доллар
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324936">
                                    Новый израильский шекель
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6325011">
                                    Новый тайваньский доллар
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6325014">
                                    Новый туркменский манат
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324972">
                                    Норвежская крона
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324963">
                                    Оманский риал
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324996">
                                    Паанга
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324973">
                                    Пакистанская рупия
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324953">
                                    Патака
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324894">
                                    Пула
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324900">
                                    Риель
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6325022">
                                    Румынский лей
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324933">
                                    Рупия
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324956">
                                    Руфия
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324990">
                                    Рэнд
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324866">
                                    СДР (специальные права заимствования)
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324915">
                                    Сальвадорский колон
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324984">
                                    Саудовский риял
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324942">
                                    Северокорейская вона
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324985">
                                    Сейшельская рупия
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6325019">
                                    Сербский динар
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324987">
                                    Сингапурский доллар
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324994">
                                    Сирийский фунт
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324977">
                                    Соль
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324945">
                                    Сом
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324989">
                                    Сомалийский шиллинг
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324871">
                                    Сомони
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6325017">
                                    Суданский фунт
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324867">
                                    Суринамский доллар
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324888">
                                    Така
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6325008">
                                    Тала
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6325004">
                                    Танзанийский шиллинг
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324939">
                                    Тенге
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324960">
                                    Тугрик
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324999">
                                    Тунисский динар
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6325023">
                                    Турецкая лира
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6325000">
                                    Угандийский шиллинг
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="23232715">
                                    Угия
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324957">
                                    Угия
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6325007">
                                    Узбекский сум
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6325006">
                                    Уругвайское песо
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6325018">
                                    Уругвайское песо в индексированных единицах
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324978">
                                    Филиппинское песо
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324930">
                                    Форинт
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324921">
                                    Франк Джибути
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6325024">
                                    Франк КФА ВЕАС
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324864">
                                    Франк КФА ВСЕАО
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324865">
                                    Франк КФП
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324981">
                                    Франк Руанды
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324982">
                                    Фунт Святой Елены.
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324919">
                                    Фунт Фолклендских островов
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6325003">
                                    Фунт стерлингов
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324912">
                                    Чешская крона
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324905">
                                    Чилийское песо
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324992">
                                    Шведская крона
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324993">
                                    Швейцарский франк
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324904">
                                    Шри-ланкийская рупия
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324902">
                                    Эскудо Кабо-Верде
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324916">
                                    Эфиопский быр
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324906">
                                    Юань
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="9146330">
                                    Южносуданский фунт
                                </span>
                            </li>
                        
                            <li>
                                <span class="tuningQuickSearchTitle currencyChangecurrencyId currencyChange" id="6324937">
                                    Ямайский доллар
                                </span>
                            </li>
                        
                    </ul>
                </div>
            </div>
            <input type="hidden" name="currencyId" id="currencyId" value="-1">
        
    </div>

</li>
<script type="text/javascript">
    $("#contextSearchcurrencyId").keyup(function () {
        var elements = $(".tuningQuickSearchTitle.currencyChangecurrencyId");
        var value = $('#contextSearchcurrencyId').val().toLowerCase();
        for (var i = 0; i < elements.length; i++) {
            var item = $(elements[i]).text().toLowerCase();
            if (item.indexOf(value) > -1) {
                $(elements[i]).parent().css('display', '');
                continue;
            }
            $(elements[i]).parent().css('display', 'none');
        }
    })

</script>

                

                    
                    
                    
                    






















<li id="selectedSubjectsTag" class="subjectsEventListener  ppRf615_tag search_tag" style="display: none;">
    <label class="vAlignTop padTop8">Предмет электронного аукциона:</label>
    <div class="manySelect width630 inlineBlock">
        <div class="collapsed height30">
            <span class="msExpandButton"></span>
            
                
                    
                
                
            
            <span data-initial="Выберите одно или несколько значений" title="Выберите одно или несколько значений" class="msPlaceholder">Выберите одно или несколько значений</span>
        </div>
        <div class="selectChose">
            <div class="expanded selectedSubjectsExpanded">
                <ul id="selectedSubjectsTagDataContainer">
                    
                        <li>
                            <label class="customCheckbox fullWidth">
                                <input type="checkbox" name="region_selectedSubjects_21959484" value="region_selectedSubjects_21959484" id="region_selectedSubjects_21959484" class="checkbox-item">
                                <label style="width: calc(100% - 50px) !important;" for="region_selectedSubjects_21959484">Оказание услуг и (или) выполнение работ по капитальному ремонту общего имущества многоквартирных домов
                                </label>
                            </label>
                        </li>
                    
                        <li>
                            <label class="customCheckbox fullWidth">
                                <input type="checkbox" name="region_selectedSubjects_21959485" value="region_selectedSubjects_21959485" id="region_selectedSubjects_21959485" class="checkbox-item">
                                <label style="width: calc(100% - 50px) !important;" for="region_selectedSubjects_21959485">Оказание услуг и (или) выполнение работ по капитальному ремонту общего имущества многоквартирных домов, являющихся объектами культурного наследия, выявленными объектами культурного наследия
                                </label>
                            </label>
                        </li>
                    
                        <li>
                            <label class="customCheckbox fullWidth">
                                <input type="checkbox" name="region_selectedSubjects_21959486" value="region_selectedSubjects_21959486" id="region_selectedSubjects_21959486" class="checkbox-item">
                                <label style="width: calc(100% - 50px) !important;" for="region_selectedSubjects_21959486">Выполнение работ и (или) оказание услуг по ремонту, замене, модернизации лифтов, ремонту лифтовых шахт, машинных и блочных помещений  (ремонт (замена, модернизация) лифтов)
                                </label>
                            </label>
                        </li>
                    
                        <li>
                            <label class="customCheckbox fullWidth">
                                <input type="checkbox" name="region_selectedSubjects_21959487" value="region_selectedSubjects_21959487" id="region_selectedSubjects_21959487" class="checkbox-item">
                                <label style="width: calc(100% - 50px) !important;" for="region_selectedSubjects_21959487">Выполнение работ и (или) оказание услуг по оценке технического состояния,  разработке проектной документации на проведение капитального ремонта общего имущества многоквартирных домов, в том числе по ремонту (замене, модернизации) лифтов
                                </label>
                            </label>
                        </li>
                    
                
                    
                        <li>
                            <label class="customCheckbox fullWidth">
                                <input type="checkbox" name="region_selectedSubjects_21959489" value="region_selectedS
                                ubjects_21959489" id="region_selectedSubjects_21959489" class="checkbox-item">
                                <label style="width: calc(100% - 50px) !important;" for="region_selectedSubjects_
                                21959489">Выполнение работ по оценке соответствия лифтов требованиям технического 
                                регламента Таможенного союза 011/2011 «Безопасность лифтов» (ТР ТС 011/2011), утв
                                ержденного решением Комиссии Таможенного союза от 18 октября 2011 г. N 824 «О прин
                                ятии технического регламента Таможенного союза «Безопасность лифтов»
                                </label>
                            </label>
                        </li>
                    
                        <li>
                            <label class="customCheckbox fullWidth">
                                <input type="checkbox" name="region_selectedSubjects_21959490" value="region_selectedSubjects_21959490" id="region_selectedSubjects_21959490" class="checkbox-item">
                                <label style="width: calc(100% - 50px) !important;" for="region_selectedSubjects_21959490">Оказание услуг по осуществлению строительного контроля
                                </label>
                            </label>
                        </li>
                    
                        <li>
                            <label class="customCheckbox fullWidth">
                                <input type="checkbox" name="region_selectedSubjects_21959491" value="region_selectedSu
                                bjects_21959491" id="region_selectedSubjects_21959491" class="checkbox-item">
                                <label style="width: calc(100% - 50px) !important;" for="region_selectedSubjects_219594
                                91">Оказание услуг и (или) выполнение работ по оценке технического состояния многокварт
                                ирных домов, разработке проектной документации на проведение капитального ремонта 
                                общего имущества многоквартирных домов, капитальному ремонту общего имущества 
                                многоквартирных домов
                                </label>
                            </label>
                        </li>
                    
                        <li>
                            <label class="customCheckbox fullWidth">
                                <input type="checkbox" name="region_selectedSubjects_27517303" value="region_selectedSu
                                bjects_27517303" id="region_selectedSubjects_27517303" class="checkbox-item">
                                <label style="width: calc(100% - 50px) !important;" for="region_selectedSubjects_275173
                                03">Оказание услуг и (или) выполнение работ по оценке технического состояния, разработ
                                ке проектной документации на проведение капитального ремонта общего имущества многоква
                                ртирных домов, являющихся объектами культурного наследия, выявленными объектами культу
                                рного наследия, капитальному ремонту общего имущества многоквартирных домов, являющихс
                                я объектами культурного наследия, выявленными объектами культурного наследия
                                </label>
                            </label>
                        </li>
                    
                        <li>
                            <label class="customCheckbox fullWidth">
                                <input type="checkbox" name="region_selectedSubjects_28985769" value="region_selectedSu
                                bjects_28985769" id="region_selectedSubjects_28985769" class="checkbox-item">
                                <label style="width: calc(100% - 50px) !important;" for="region_selectedSubjects_289857
                                69">Оказание услуг и (или) выполнение работ по оценке технического состояния конструкти
                                вных элементов лифтовой шахты, разработке проектной документации на ремонт (замену, мод
                                ернизацию) лифтов , выполнению работ по ремонту (замене, модернизации) лифтов
                                </label>
                            </label>
                        </li>
                    
                </ul>
            </div>
            <div id="selectedSubjectsSelectBtn" class="msButtonIn"><span class="btnBtn blueBtn">Выбрать</span>
            </div>
        </div>
    </div>
    <input type="hidden" name="selectedSubjects" id="selectedSubjects" value="">
</li>
<script type="text/javascript">
    $(document).ready(
        function () {
            $("#selectedSubjectsTag").on("setDefaultValues", function () {
                $("#selectedSubjectsTagDataContainer :checkbox").prop("checked", false);
                setManySelectPlaceholderText("selectedSubjectsSelectBtn");
                $('#selectedSubjects').val('');
            });

            
            $("#selectedSubjectsTag").bind("subjectsEvent", function (e, data) {
                _selectedSubjectsChangeRegionsByDistricts(data.districtsList);
            });
            

            $("#selectedSubjectsSelectBtn").click(function (e) {
                setHiddenValue($("div.selectedSubjectsExpanded input:checked"), $("#selectedSubjects"), 8 + 16);
                _selectedSubjectsDispathEvent(e);
            });
            setManySelectPlaceholderText("selectedSubjectsSelectBtn");
            setHiddenValue($("div.selectedSubjectsExpanded input:checked"), $("#selectedSubjects"), 8 + 16);

            $('li#selectedSubjectsTag input[type=checkbox]').on("delete", function (event) {
                this.removeAttribute("checked");
                var subjectId = $(this).attr('id').substr(8 + 16);
                $('#selectedSubjects').val($('#selectedSubjects').val().replace(subjectId, ""));

            });
        }
    );

    function _selectedSubjectsChangeRegionsByDistricts(districtsList) {
        var ajaxUrl = '/epz/order/quicksearch/tagupdate.html?dtoClass=&subjects=' + districtsList;
        $.ajax({
            url: ajaxUrl,
            dataType: 'html',
            success: function (html) {
                var containerSelector = "#selectedSubjectsTagDataContainer";
                var liData = $(html).find(containerSelector + " li");
                $(containerSelector).html(liData);
                setManySelectPlaceholderText("selectedSubjectsSelectBtn");
                $("#" + "selectedSubjects").val("");
                _selectedSubjectsDispathEvent();
            }
        });
    }
    ;

    function _selectedSubjectsDispathEvent(e) {
        var checked = $("div.selectedSubjectsExpanded input:checked");
        var outputValues = _createDropDownChecksValues(checked, 8 + 16);
        $('#searchOptionsEditContainer .selectedSubjectsEventListener').each(function () {
            $(this).trigger("selectedSubjectsEvent", {subjectsList: outputValues});
        });
    }
    ;
</script>


                

                    
                    
                    
                    




















    
        
    
    




<li id="agencyTag" class="  hide_MS-clear">
    
        
            














<label class="vAlignMiddle">Организация, осуществляющая размещение:</label>

    
        



















    



<span role="status" aria-live="polite" class="ui-helper-hidden-accessible"></span><input name="agencyTitle" type="text" maxlength="255" class="organizationAutocomplete hint width_inputs ui-autocomplete-input" title="Введите полностью или часть полного или сокращенного наименования организации, ИНН" id="agency" value="" style="width: 605px; color: rgb(153, 153, 153);" data-validate="{&quot;chooseOrganization&quot;: &quot;true&quot;}" data-rule-maxlength="255" data-msg-maxlength="Введите не более {0} символов" data-disable-onkeyup-validate="true" data-disable-onfocusout-validate="true" autocomplete="off">
<div id="agencyParams" style="display: none;">
    <input type="hidden" class="organizationType" value="ALL">
</div>
<input type="hidden" name="agencyCode" id="agencyCpz" value="">
<input type="hidden" name="agencyFz94id" id="agencyFz94Id" value="">
<input type="hidden" name="agencyFz223id" id="agencyFz223Id" value="">
<input type="hidden" name="agencyInn" id="agencyInn" value="">


    
    
        <a href="/epz/organization/chooseOrganization/chooseOrganizationDialog.html?fieldName=agency&amp;organizationType=ALL&amp;dialogTitle=&amp;noPlaceTitle=false" class="zoom" initialhref="/epz/organization/chooseOrganization/chooseOrganizationDialog.html?fieldName=agency&amp;organizationType=ALL&amp;dialogTitle=&amp;noPlaceTitle=false" id="agencyLink" title="Выбор организации из справочника">
        </a>
    

    
    

<ul id="agencyError">
    
</ul>
        
        
    
</li>

<script type="text/javascript">
    var selectOrganizationListener = function (newValue) {
        if (typeof(selectOrganizationExtParamsListener) == "function") {
            selectOrganizationExtParamsListener.call(undefined, newValue);
        }
    };
    $(document).ready(function () {
        epzCommonChooseOrganization.setNoPlaceFlag(false);
        if (typeof(placeOfSearchChangeFunc) != "function") {
            epzCommonChooseOrganization.initCommonChooseOrganizationWithSelectCallback(
                "agency",
                "FZ_44,FZ_223".split(","),
                selectOrganizationListener
            );
        } else {
            epzCommonChooseOrganization.initCommonChooseOrganizationByFunc(
                "agency",
                placeOfSearchChangeFunc,
                selectOrganizationListener
            )
        }
        $("#" + "agency" + "Tag").on("setDefaultValues", function () {
            epzCommonChooseOrganization.clearOrganizationFields("agency");
        }).on("delete", function () {
            epzCommonChooseOrganization.clearOrganizationFields("agency");
        });
    });
</script>

                

                    
                    
                    
                    





















<script type="text/javascript">
    $(document).ready(function () {
        $("#" + "budgetUnionState" + "Tag").on("setDefaultValues", function () {
            $("#" + "budgetUnionState").prop("checked", "");
        });

        $("#budgetUnionStateTag input[type='checkbox']").on("delete", function(event) {
            $(this).prop("checked", false);
        });
    });
</script>

<li id="budgetUnionStateTag" class=" fz44_tag search_tag" style="display: none;"><label for="budgetUnionState">
    Закупка за счет средств бюджета Союзного государства:</label>
    <ul class="lowList">
        <li class="customCheckbox">
            <input id="budgetUnionState" type="checkbox" name="budgetUnionState">
            <label for="budgetUnionState"></label>
        </li>
    </ul>
</li>

                

                    
                    
                    
                    






















<li id="regionsTag" class="EventListener  ">
    <label class="vAlignTop padTop8">Субъект РФ Заказчика:</label>
    <div class="manySelect width630 inlineBlock">
        <div class="collapsed height30">
            <span class="msExpandButton"></span>
            
                
                    
                
                
            
            <span data-initial="Выберите один или несколько субъектов РФ" title="Выберите один или несколько субъектов РФ" class="msPlaceholder">Выберите один или несколько субъектов РФ</span>
        </div>
        <div class="selectChose">
            <div class="expanded regionsExpanded">
                <ul id="regionsTagDataContainer">
                    <li>
                        <label class="customCheckbox">
                            <input type="checkbox" name="region_regions_not_selected" value="region_regions_not_selected" id="region_regions_not_selected" class="checkbox-item not-selected-many-select-item">
                            <label style="width: calc(100% - 50px) !important;" for="region_regions_not_selected">Не выбран
                            </label>
                        </label>
                    </li>
                    
                        <li>
                            <label class="customCheckbox">
                                <input type="checkbox" name="region_regions_5277349" value="region_regions_5277349" id="region_regions_5277349" class="checkbox-item ">
                                <label style="width: calc(100% - 50px) !important;" for="region_regions_5277349">Адыгея Респ
                                </label>
                            </label>
                        </li>
                    
                        <li>
                            <label class="customCheckbox">
                                <input type="checkbox" name="region_regions_5277385" value="region_regions_5277385" id="region_regions_5277385" class="checkbox-item ">
                                <label style="width: calc(100% - 50px) !important;" for="region_regions_5277385">Алтай Респ
                                </label>
                            </label>
                        </li>
                    
                        <li>
                            <label class="customCheckbox">
                                <input type="checkbox" name="region_regions_5277388" value="region_regions_5277388" id="region_regions_5277388" class="checkbox-item ">
                                <label style="width: calc(100% - 50px) !important;" for="region_regions_5277388">Алтайский край
                                </label>
                            </label>
                        </li>
                    
                        <li>
                            <label class="customCheckbox">
                                <input type="checkbox" name="region_regions_5277403" value="region_regions_5277403" id="region_regions_5277403" class="checkbox-item ">
                                <label style="width: calc(100% - 50px) !important;" for="region_regions_5277403">Амурская обл
                                </label>
                            </label>
                        </li>
                    
                        <li>
                            <label class="customCheckbox">
                                <input type="checkbox" name="region_regions_5277339" value="region_regions_5277339" id="region_regions_5277339" class="checkbox-item ">
                                <label style="width: calc(100% - 50px) !important;" for="region_regions_5277339">Архангельская обл
                                </label>
                            </label>
                        </li>
                    
                        <li>
                            <label class="customCheckbox">
                                <input type="checkbox" name="region_regions_5277355" value="region_regions_5277355" id="region_regions_5277355" class="checkbox-item ">
                                <label style="width: calc(100% - 50px) !important;" for="region_regions_5277355">Астраханская обл
                                </label>
                            </label>
                        </li>
                    
                        <li>
                            <label class="customCheckbox">
                                <input type="checkbox" name="region_regions_5277409" value="region_regions_5277409" id="region_regions_5277409" class="checkbox-item ">
                                <label style="width: calc(100% - 50px) !important;" for="region_regions_5277409">Байконур г
                                </label>
                            </label>
                        </li>
                    
                        <li>
                            <label class="customCheckbox">
                                <input type="checkbox" name="region_regions_5277363" value="region_regions_5277363" id="region_regions_5277363" class="checkbox-item ">
                                <label style="width: calc(100% - 50px) !important;" for="region_regions_5277363">Башкортостан Респ
                                </label>
                            </label>
                        </li>
                    
                        <li>
                            <label class="customCheckbox">
                                <input type="checkbox" name="region_regions_5277318" value="region_regions_5277318" id="region_regions_5277318" class="checkbox-item ">
                                <label style="width: calc(100% - 50px) !important;" for="region_regions_5277318">Белгородская обл
                                </label>
                            </label>
                        </li>
                    
                        <li>
                            <label class="customCheckbox">
                                <input type="checkbox" name="region_regions_5277319" value="region_regions_5277319" id="region_regions_5277319" class="checkbox-item ">
                                <label style="width: calc(100% - 50px) !important;" for="region_regions_5277319">Брянская обл
                                </label>
                            </label>
                        </li>
                    
                        <li>
                            <label class="customCheckbox">
                                <input type="checkbox" name="region_regions_5277397" value="region_regions_5277397" id="region_regions_5277397" class="checkbox-item ">
                                <label style="width: calc(100% - 50px) !important;" for="region_regions_5277397">Бурятия Респ
                                </label>
                            </label>
                        </li>
                    
                        <li>
                            <label class="customCheckbox">
                                <input type="checkbox" name="region_regions_5277320" value="region_regions_5277320" id="region_regions_5277320" class="checkbox-item ">
                                <label style="width: calc(100% - 50px) !important;" for="region_regions_5277320">Владимирская обл
                                </label>
                            </label>
                        </li>
                    
                        <li>
                            <label class="customCheckbox">
                                <input type="checkbox" name="region_regions_5277356" value="region_regions_5277356" id="region_regions_5277356" class="checkbox-item ">
                                <label style="width: calc(100% - 50px) !important;" for="region_regions_5277356">Волгоградская обл
                                </label>
                            </label>
                        </li>
                    
                        <li>
                            <label class="customCheckbox">
                                <input type="checkbox" name="region_regions_5277340" value="region_regions_5277340" id="region_regions_5277340" class="checkbox-item ">
                                <label style="width: calc(100% - 50px) !important;" for="region_regions_5277340">Вологодская обл
                                </label>
                            </label>
                        </li>
                    
                        <li>
                            <label class="customCheckbox">
                                <input type="checkbox" name="region_regions_5277321" value="region_regions_5277321" id="region_regions_5277321" class="checkbox-item ">
                                <label style="width: calc(100% - 50px) !important;" for="region_regions_5277321">Воронежская обл
                                </label>
                            </label>
                        </li>
                    
                        <li>
                            <label class="customCheckbox">
                                <input type="checkbox" name="region_regions_5277361" value="region_regions_5277361" id="region_regions_5277361" class="checkbox-item ">
                                <label style="width: calc(100% - 50px) !important;" for="region_regions_5277361">Дагестан Респ
                                </label>
                            </label>
                        </li>
                    
                        <li>
                            <label class="customCheckbox">
                                <input type="checkbox" name="region_regions_5277407" value="region_regions_5277407" id="region_regions_5277407" class="checkbox-item ">
                                <label style="width: calc(100% - 50px) !important;" for="region_regions_5277407">Еврейская Аобл
                                </label>
                            </label>
                        </li>
                    
                        <li>
                            <label class="customCheckbox">
                                <input type="checkbox" name="region_regions_5277394" value="region_regions_5277394" id="region_regions_5277394" class="checkbox-item ">
                                <label style="width: calc(100% - 50px) !important;" for="region_regions_5277394">Забайкальский край
                                </label>
                            </label>
                        </li>
                    
                        <li>
                            <label class="customCheckbox">
                                <input type="checkbox" name="region_regions_5277322" value="region_regions_5277322" id="region_regions_5277322" class="checkbox-item ">
                                <label style="width: calc(100% - 50px) !important;" for="region_regions_5277322">Ивановская обл
                                </label>
                            </label>
                        </li>
                    
                        <li>
                            <label class="customCheckbox">
                                <input type="checkbox" name="region_regions_5277350" value="region_regions_5277350" id="region_regions_5277350" class="checkbox-item ">
                                <label style="width: calc(100% - 50px) !important;" for="region_regions_5277350">Ингушетия Респ
                                </label>
                            </label>
                        </li>
                    
                        <li>
                            <label class="customCheckbox">
                                <input type="checkbox" name="region_regions_5277389" value="region_regions_5277389" id="region_regions_5277389" class="checkbox-item ">
                                <label style="width: calc(100% - 50px) !important;" for="region_regions_5277389">Иркутская обл
                                </label>
                            </label>
                        </li>
                    
                        <li>
                            <label class="customCheckbox">
                                <input type="checkbox" name="region_regions_5277351" value="region_regions_5277351" id="region_regions_5277351" class="checkbox-item ">
                                <label style="width: calc(100% - 50px) !important;" for="region_regions_5277351">Кабардино-Балкарская Респ
                                </label>
                            </label>
                        </li>
                    
                        <li>
                            <label class="customCheckbox">
                                <input type="checkbox" name="region_regions_5277341" value="region_regions_5277341" id="region_regions_5277341" class="checkbox-item ">
                                <label style="width: calc(100% - 50px) !important;" for="region_regions_5277341">Калининградская обл
                                </label>
                            </label>
                        </li>
                    
                        <li>
                            <label class="customCheckbox">
                                <input type="checkbox" name="region_regions_5277360" value="region_regions_5277360" id="region_regions_5277360" class="checkbox-item ">
                                <label style="width: calc(100% - 50px) !important;" for="region_regions_5277360">Калмыкия Респ
                                </label>
                            </label>
                        </li>
                    
                        <li>
                            <label class="customCheckbox">
                                <input type="checkbox" name="region_regions_5277323" value="region_regions_5277323" id="region_regions_5277323" class="checkbox-item ">
                                <label style="width: calc(100% - 50px) !important;" for="region_regions_5277323">Калужская обл
                                </label>
                            </label>
                        </li>
                    
                        <li>
                            <label class="customCheckbox">
                                <input type="checkbox" name="region_regions_5277404" value="region_regions_5277404" id="region_regions_5277404" class="checkbox-item ">
                                <label style="width: calc(100% - 50px) !important;" for="region_regions_5277404">Камчатский край
                                </label>
                            </label>
                        </li>
                    
                        <li>
                            <label class="customCheckbox">
                                <input type="checkbox" name="region_regions_5277352" value="region_regions_5277352" id="region_regions_5277352" class="checkbox-item ">
                                <label style="width: calc(100% - 50px) !important;" for="region_regions_5277352">Карачаево-Черкесская Респ
                                </label>
                            </label>
                        </li>
                    
                        <li>
                            <label class="customCheckbox">
                                <input type="checkbox" name="region_regions_5277337" value="region_regions_5277337" id="region_regions_5277337" class="checkbox-item ">
                                <label style="width: calc(100% - 50px) !important;" for="region_regions_5277337">Карелия Респ
                                </label>
                            </label>
                        </li>
                    
                        <li>
                            <label class="customCheckbox">
                                <input type="checkbox" name="region_regions_5277390" value="region_regions_5277390" id="region_regions_5277390" class="checkbox-item ">
                                <label style="width: calc(100% - 50px) !important;" for="region_regions_5277390">Кемеровская обл
                                </label>
                            </label>
                        </li>
                    
                        <li>
                            <label class="customCheckbox">
                                <input type="checkbox" name="region_regions_5277369" value="region_regions_5277369" id="region_regions_5277369" class="checkbox-item ">
                                <label style="width: calc(100% - 50px) !important;" for="region_regions_5277369">Кировская обл
                                </label>
                            </label>
                        </li>
                    
                        <li>
                            <label class="customCheckbox">
                                <input type="checkbox" name="region_regions_5277338" value="region_regions_5277338" id="region_regions_5277338" class="checkbox-item ">
                                <label style="width: calc(100% - 50px) !important;" for="region_regions_5277338">Коми Респ
                                </label>
                            </label>
                        </li>
                    
                        <li>
                            <label class="customCheckbox">
                                <input type="checkbox" name="region_regions_5277324" value="region_regions_5277324" id="region_regions_5277324" class="checkbox-item ">
                                <label style="width: calc(100% - 50px) !important;" for="region_regions_5277324">Костромская обл
                                </label>
                            </label>
                        </li>
                    
                        <li>
                            <label class="customCheckbox">
                                <input type="checkbox" name="region_regions_5277353" value="region_regions_5277353" id="region_regions_5277353" class="checkbox-item ">
                                <label style="width: calc(100% - 50px) !important;" for="region_regions_5277353">Краснодарский край
                                </label>
                            </label>
                        </li>
                    
                        <li>
                            <label class="customCheckbox">
                                <input type="checkbox" name="region_regions_5277398" value="region_regions_5277398" id="region_regions_5277398" class="checkbox-item ">
                                <label style="width: calc(100% - 50px) !important;" for="region_regions_5277398">Красноярский край
                                </label>
                            </label>
                        </li>
                    
                        <li>
                            <label class="customCheckbox">
                                <input type="checkbox" name="region_regions_8408974" value="region_regions_8408974" id="region_regions_8408974" class="checkbox-item ">
                                <label style="width: calc(100% - 50px) !important;" for="region_regions_8408974">Крым Респ
                                </label>
                            </label>
                        </li>
                    
                        <li>
                            <label class="customCheckbox">
                                <input type="checkbox" name="region_regions_5277378" value="region_regions_5277378" id="region_regions_5277378" class="checkbox-item ">
                                <label style="width: calc(100% - 50px) !important;" for="region_regions_5277378">Курганская обл
                                </label>
                            </label>
                        </li>
                    
                        <li>
                            <label class="customCheckbox">
                                <input type="checkbox" name="region_regions_5277325" value="region_regions_5277325" id="region_regions_5277325" class="checkbox-item ">
                                <label style="width: calc(100% - 50px) !important;" for="region_regions_5277325">Курская обл
                                </label>
                            </label>
                        </li>
                    
                        <li>
                            <label class="customCheckbox">
                                <input type="checkbox" name="region_regions_5277342" value="region_regions_5277342" id="region_regions_5277342" class="checkbox-item ">
                                <label style="width: calc(100% - 50px) !important;" for="region_regions_5277342">Ленинградская обл
                                </label>
                            </label>
                        </li>
                    
                        <li>
                            <label class="customCheckbox">
                                <input type="checkbox" name="region_regions_5277326" value="region_regions_5277326" id="region_regions_5277326" class="checkbox-item ">
                                <label style="width: calc(100% - 50px) !important;" for="region_regions_5277326">Липецкая обл
                                </label>
                            </label>
                        </li>
                    
                        <li>
                            <label class="customCheckbox">
                                <input type="checkbox" name="region_regions_5277405" value="region_regions_5277405" id="region_regions_5277405" class="checkbox-item ">
                                <label style="width: calc(100% - 50px) !important;" for="region_regions_5277405">Магаданская обл
                                </label>
                            </label>
                        </li>
                    
                        <li>
                            <label class="customCheckbox">
                                <input type="checkbox" name="region_regions_5277364" value="region_regions_5277364" id="region_regions_5277364" class="checkbox-item ">
                                <label style="width: calc(100% - 50px) !important;" for="region_regions_5277364">Марий Эл Респ
                                </label>
                            </label>
                        </li>
                    
                        <li>
                            <label class="customCheckbox">
                                <input type="checkbox" name="region_regions_5277365" value="region_regions_5277365" id="region_regions_5277365" class="checkbox-item ">
                                <label style="width: calc(100% - 50px) !important;" for="region_regions_5277365">Мордовия Респ
                                </label>
                            </label>
                        </li>
                    
                        <li>
                            <label class="customCheckbox">
                                <input type="checkbox" name="region_regions_5277335" value="region_regions_5277335" id="region_regions_5277335" class="checkbox-item ">
                                <label style="width: calc(100% - 50px) !important;" for="region_regions_5277335">Москва
                                </label>
                            </label>
                        </li>
                    
                        <li>
                            <label class="customCheckbox">
                                <input type="checkbox" name="region_regions_5277327" value="region_regions_5277327" id="region_regions_5277327" class="checkbox-item ">
                                <label style="width: calc(100% - 50px) !important;" for="region_regions_5277327">Московская обл
                                </label>
                            </label>
                        </li>
                    
                        <li>
                            <label class="customCheckbox">
                                <input type="checkbox" name="region_regions_5277343" value="region_regions_5277343" id="region_regions_5277343" class="checkbox-item ">
                                <label style="width: calc(100% - 50px) !important;" for="region_regions_5277343">Мурманская обл
                                </label>
                            </label>
                        </li>
                    
                        <li>
                            <label class="customCheckbox">
                                <input type="checkbox" name="region_regions_5277345" value="region_regions_5277345" id="region_regions_5277345" class="checkbox-item ">
                                <label style="width: calc(100% - 50px) !important;" for="region_regions_5277345">Ненецкий АО
                                </label>
                            </label>
                        </li>
                    
                        <li>
                            <label class="customCheckbox">
                                <input type="checkbox" name="region_regions_5277370" value="region_regions_5277370" id="region_regions_5277370" class="checkbox-item ">
                                <label style="width: calc(100% - 50px) !important;" for="region_regions_5277370">Нижегородская обл
                                </label>
                            </label>
                        </li>
                    
                        <li>
                            <label class="customCheckbox">
                                <input type="checkbox" name="region_regions_5277346" value="region_regions_5277346" id="region_regions_5277346" class="checkbox-item ">
                                <label style="width: calc(100% - 50px) !important;" for="region_regions_5277346">Новгородская обл
                                </label>
                            </label>
                        </li>
                    
                        <li>
                            <label class="customCheckbox">
                                <input type="checkbox" name="region_regions_5277391" value="region_regions_5277391" id="region_regions_5277391" class="checkbox-item ">
                                <label style="width: calc(100% - 50px) !important;" for="region_regions_5277391">Новосибирская обл
                                </label>
                            </label>
                        </li>
                    
                        <li>
                            <label class="customCheckbox">
                                <input type="checkbox" name="region_regions_5277392" value="region_regions_5277392" id="region_regions_5277392" class="checkbox-item ">
                                <label style="width: calc(100% - 50px) !important;" for="region_regions_5277392">Омская обл
                                </label>
                            </label>
                        </li>
                    
                        <li>
                            <label class="customCheckbox">
                                <input type="checkbox" name="region_regions_5277371" value="region_regions_5277371" id="region_regions_5277371" class="checkbox-item ">
                                <label style="width: calc(100% - 50px) !important;" for="region_regions_5277371">Оренбургская обл
                                </label>
                            </label>
                        </li>
                    
                        <li>
                            <label class="customCheckbox">
                                <input type="checkbox" name="region_regions_5277328" value="region_regions_5277328" id="region_regions_5277328" class="checkbox-item ">
                                <label style="width: calc(100% - 50px) !important;" for="region_regions_5277328">Орловская обл
                                </label>
                            </label>
                        </li>
                    
                        <li>
                            <label class="customCheckbox">
                                <input type="checkbox" name="region_regions_5277372" value="region_regions_5277372" id="region_regions_5277372" class="checkbox-item ">
                                <label style="width: calc(100% - 50px) !important;" for="region_regions_5277372">Пензенская обл
                                </label>
                            </label>
                        </li>
                    
                        <li>
                            <label class="customCheckbox">
                                <input type="checkbox" name="region_regions_5277373" value="region_regions_5277373" id="region_regions_5277373" class="checkbox-item ">
                                <label style="width: calc(100% - 50px) !important;" for="region_regions_5277373">Пермский край
                                </label>
                            </label>
                        </li>
                    
                        <li>
                            <label class="customCheckbox">
                                <input type="checkbox" name="region_regions_5277401" value="region_regions_5277401" id="region_regions_5277401" class="checkbox-item ">
                                <label style="width: calc(100% - 50px) !important;" for="region_regions_5277401">Приморский край
                                </label>
                            </label>
                        </li>
                    
                        <li>
                            <label class="customCheckbox">
                                <input type="checkbox" name="region_regions_5277344" value="region_regions_5277344" id="region_regions_5277344" class="checkbox-item ">
                                <label style="width: calc(100% - 50px) !important;" for="region_regions_5277344">Псковская обл
                                </label>
                            </label>
                        </li>
                    
                        <li>
                            <label class="customCheckbox">
                                <input type="checkbox" name="region_regions_5277357" value="region_regions_5277357" id="region_regions_5277357" class="checkbox-item ">
                                <label style="width: calc(100% - 50px) !important;" for="region_regions_5277357">Ростовская обл
                                </label>
                            </label>
                        </li>
                    
                        <li>
                            <label class="customCheckbox">
                                <input type="checkbox" name="region_regions_5277329" value="region_regions_5277329" id="region_regions_5277329" class="checkbox-item ">
                                <label style="width: calc(100% - 50px) !important;" for="region_regions_5277329">Рязанская обл
                                </label>
                            </label>
                        </li>
                    
                        <li>
                            <label class="customCheckbox">
                                <input type="checkbox" name="region_regions_5277374" value="region_regions_5277374" id="region_regions_5277374" class="checkbox-item ">
                                <label style="width: calc(100% - 50px) !important;" for="region_regions_5277374">Самарская обл
                                </label>
                            </label>
                        </li>
                    
                        <li>
                            <label class="customCheckbox">
                                <input type="checkbox" name="region_regions_5277347" value="region_regions_5277347" id="region_regions_5277347" class="checkbox-item ">
                                <label style="width: calc(100% - 50px) !important;" for="region_regions_5277347">Санкт-Петербург
                                </label>
                            </label>
                        </li>
                    
                        <li>
                            <label class="customCheckbox">
                                <input type="checkbox" name="region_regions_5277375" value="region_regions_5277375" id="region_regions_5277375" class="checkbox-item ">
                                <label style="width: calc(100% - 50px) !important;" for="region_regions_5277375">Саратовская обл
                                </label>
                            </label>
                        </li>
                    
                        <li>
                            <label class="customCheckbox">
                                <input type="checkbox" name="region_regions_5277400" value="region_regions_5277400" id="region_regions_5277400" class="checkbox-item ">
                                <label style="width: calc(100% - 50px) !important;" for="region_regions_5277400">Саха /Якутия/ Респ
                                </label>
                            </label>
                        </li>
                    
                        <li>
                            <label class="customCheckbox">
                                <input type="checkbox" name="region_regions_5277406" value="region_regions_5277406" id="region_regions_5277406" class="checkbox-item ">
                                <label style="width: calc(100% - 50px) !important;" for="region_regions_5277406">Сахалинская обл
                                </label>
                            </label>
                        </li>
                    
                        <li>
                            <label class="customCheckbox">
                                <input type="checkbox" name="region_regions_5277383" value="region_regions_5277383" id="region_regions_5277383" class="checkbox-item ">
                                <label style="width: calc(100% - 50px) !important;" for="region_regions_5277383">Свердловская обл
                                </label>
                            </label>
                        </li>
                    
                        <li>
                            <label class="customCheckbox">
                                <input type="checkbox" name="region_regions_8408975" value="region_regions_8408975" id="region_regions_8408975" class="checkbox-item ">
                                <label style="width: calc(100% - 50px) !important;" for="region_regions_8408975">Севастополь г
                                </label>
                            </label>
                        </li>
                    
                        <li>
                            <label class="customCheckbox">
                                <input type="checkbox" name="region_regions_5277359" value="region_regions_5277359" id="region_regions_5277359" class="checkbox-item ">
                                <label style="width: calc(100% - 50px) !important;" for="region_regions_5277359">Северная Осетия - Алания Респ
                                </label>
                            </label>
                        </li>
                    
                        <li>
                            <label class="customCheckbox">
                                <input type="checkbox" name="region_regions_5277330" value="region_regions_5277330" id="region_regions_5277330" class="checkbox-item ">
                                <label style="width: calc(100% - 50px) !important;" for="region_regions_5277330">Смоленская обл
                                </label>
                            </label>
                        </li>
                    
                        <li>
                            <label class="customCheckbox">
                                <input type="checkbox" name="region_regions_5277354" value="region_regions_5277354" id="region_regions_5277354" class="checkbox-item ">
                                <label style="width: calc(100% - 50px) !important;" for="region_regions_5277354">Ставропольский край
                                </label>
                            </label>
                        </li>
                    
                        <li>
                            <label class="customCheckbox">
                                <input type="checkbox" name="region_regions_5277331" value="region_regions_5277331" id="region_regions_5277331" class="checkbox-item ">
                                <label style="width: calc(100% - 50px) !important;" for="region_regions_5277331">Тамбовская обл
                                </label>
                            </label>
                        </li>
                    
                        <li>
                            <label class="customCheckbox">
                                <input type="checkbox" name="region_regions_5277366" value="region_regions_5277366" id="region_regions_5277366" class="checkbox-item ">
                                <label style="width: calc(100% - 50px) !important;" for="region_regions_5277366">Татарстан Респ
                                </label>
                            </label>
                        </li>
                    
                        <li>
                            <label class="customCheckbox">
                                <input type="checkbox" name="region_regions_5277332" value="region_regions_5277332" id="region_regions_5277332" class="checkbox-item ">
                                <label style="width: calc(100% - 50px) !important;" for="region_regions_5277332">Тверская обл
                                </label>
                            </label>
                        </li>
                    
                        <li>
                            <label class="customCheckbox">
                                <input type="checkbox" name="region_regions_5277393" value="region_regions_5277393" id="region_regions_5277393" class="checkbox-item ">
                                <label style="width: calc(100% - 50px) !important;" for="region_regions_5277393">Томская обл
                                </label>
                            </label>
                        </li>
                    
                        <li>
                            <label class="customCheckbox">
                                <input type="checkbox" name="region_regions_5277333" value="region_regions_5277333" id="region_regions_5277333" class="checkbox-item ">
                                <label style="width: calc(100% - 50px) !important;" for="region_regions_5277333">Тульская обл
                                </label>
                            </label>
                        </li>
                    
                        <li>
                            <label class="customCheckbox">
                                <input type="checkbox" name="region_regions_5277386" value="region_regions_5277386" id="region_regions_5277386" class="checkbox-item ">
                                <label style="width: calc(100% - 50px) !important;" for="region_regions_5277386">Тыва Респ
                                </label>
                            </label>
                        </li>
                    
                        <li>
                            <label class="customCheckbox">
                                <input type="checkbox" name="region_regions_5277379" value="region_regions_5277379" id="region_regions_5277379" class="checkbox-item ">
                                <label style="width: calc(100% - 50px) !important;" for="region_regions_5277379">Тюменская обл
                                </label>
                            </label>
                        </li>
                    
                        <li>
                            <label class="customCheckbox">
                                <input type="checkbox" name="region_regions_5277367" value="region_regions_5277367" id="region_regions_5277367" class="checkbox-item ">
                                <label style="width: calc(100% - 50px) !important;" for="region_regions_5277367">Удмуртская Респ
                                </label>
                            </label>
                        </li>
                    
                        <li>
                            <label class="customCheckbox">
                                <input type="checkbox" name="region_regions_5277376" value="region_regions_5277376" id="region_regions_5277376" class="checkbox-item ">
                                <label style="width: calc(100% - 50px) !important;" for="region_regions_5277376">Ульяновская обл
                                </label>
                            </label>
                        </li>
                    
                        <li>
                            <label class="customCheckbox">
                                <input type="checkbox" name="region_regions_5277402" value="region_regions_5277402" id="region_regions_5277402" class="checkbox-item ">
                                <label style="width: calc(100% - 50px) !important;" for="region_regions_5277402">Хабаровский край
                                </label>
                            </label>
                        </li>
                    
                        <li>
                            <label class="customCheckbox">
                                <input type="checkbox" name="region_regions_5277387" value="region_regions_5277387" id="region_regions_5277387" class="checkbox-item ">
                                <label style="width: calc(100% - 50px) !important;" for="region_regions_5277387">Хакасия Респ
                                </label>
                            </label>
                        </li>
                    
                        <li>
                            <label class="customCheckbox">
                                <input type="checkbox" name="region_regions_5277381" value="region_regions_5277381" id="region_regions_5277381" class="checkbox-item ">
                                <label style="width: calc(100% - 50px) !important;" for="region_regions_5277381">Ханты-Мансийский Автономный округ - Югра АО
                                </label>
                            </label>
                        </li>
                    
                        <li>
                            <label class="customCheckbox">
                                <input type="checkbox" name="region_regions_5277380" value="region_regions_5277380" id="region_regions_5277380" class="checkbox-item ">
                                <label style="width: calc(100% - 50px) !important;" for="region_regions_5277380">Челябинская обл
                                </label>
                            </label>
                        </li>
                    
                        <li>
                            <label class="customCheckbox">
                                <input type="checkbox" name="region_regions_5277358" value="region_regions_5277358" id="region_regions_5277358" class="checkbox-item ">
                                <label style="width: calc(100% - 50px) !important;" for="region_regions_5277358">Чеченская Респ
                                </label>
                            </label>
                        </li>
                    
                        <li>
                            <label class="customCheckbox">
                                <input type="checkbox" name="region_regions_5277368" value="region_regions_5277368" id="region_regions_5277368" class="checkbox-item ">
                                <label style="width: calc(100% - 50px) !important;" for="region_regions_5277368">Чувашская Республика - Чувашия
                                </label>
                            </label>
                        </li>
                    
                        <li>
                            <label class="customCheckbox">
                                <input type="checkbox" name="region_regions_5277408" value="region_regions_5277408" id="region_regions_5277408" class="checkbox-item ">
                                <label style="width: calc(100% - 50px) !important;" for="region_regions_5277408">Чукотский АО
                                </label>
                            </label>
                        </li>
                    
                        <li>
                            <label class="customCheckbox">
                                <input type="checkbox" name="region_regions_5277382" value="region_regions_5277382" id="region_regions_5277382" class="checkbox-item ">
                                <label style="width: calc(100% - 50px) !important;" for="region_regions_5277382">Ямало-Ненецкий АО
                                </label>
                            </label>
                        </li>
                    
                        <li>
                            <label class="customCheckbox">
                                <input type="checkbox" name="region_regions_5277334" value="region_regions_5277334" id="region_regions_5277334" class="checkbox-item ">
                                <label style="width: calc(100% - 50px) !important;" for="region_regions_5277334">Ярославская обл
                                </label>
                            </label>
                        </li>
                    
                </ul>
            </div>
            <div id="regionsSelectBtn" class="msButtonIn"><span class="btnBtn blueBtn">Выбрать</span>
            </div>
        </div>
    </div>
    <input type="hidden" name="regions" id="regions" value="">
    <input type="hidden" name="regionDeleted" id="regionDeleted" value="false">
</li>
<script type="text/javascript">
    $(document).ready(function () {
            $("#regionsTag").on("setDefaultValues", function () {
                $("#regionsTagDataContainer :checkbox").prop("checked", false);
                setManySelectPlaceholderText("regionsSelectBtn");
                $('#regions').val('');
            });

            
            $("#regionsTag").bind("Event", function (e, data) {
                _regionsChangeRegionsByDistricts(data.districtsList);
            });
            

            $("#regionsSelectBtn").click(function (e) {
                setHiddenValue($("div.regionsExpanded input:checked"), $("#regions"), 8 + 7);
                _regionsDispathEvent(e);
            });
            setManySelectPlaceholderText("regionsSelectBtn");
            setHiddenValue($("div.regionsExpanded input:checked"), $("#regions"), 8 + 7);

            $('li#regionsTag input[type=checkbox]').on("delete", function (event) {
                this.removeAttribute("checked");
                var regionId = $(this).attr('id').substr(8 + 7);
                var userRegionId = $.cookie("userRegionId");
                var doNotUseRegionToFind = $.cookie("doNotUseRegionToFind");
                if (regionId == userRegionId && doNotUseRegionToFind == 'false') {
                    $("#regionDeleted").val("true");
                }
                $('#regions').val($('#regions').val().replace(regionId, ""));
            });

            $("#regionsTagDataContainer li").on('click', function () {
                var $this = $(this);
                choiceRestriction($this);
                var inputJqr = $(this).find("input:checkbox");
                if (inputJqr.attr("id") === "region_regions_not_selected") {
                    _regionsClearRegionsChecked();
                } else {
                    _regionsAddHiddenValueOnChecked($this);
                }
                _regionsRefreshPlaceholder($this);
            });
        }
    );

    function _regionsAddHiddenValueOnChecked($this) {
        $("#region_regions_not_selected").removeAttr("checked");
        var selectedListJqr = _regionsGetCheckedListJqr($this)
        setHiddenValue(selectedListJqr, $("#regions"), 8 + 7);
    }

    function _regionsClearRegionsChecked() {
        $("div.regionsExpanded input:checked")
            .not("#region_regions_not_selected")
            .removeAttr("checked");
        setHiddenValue($([]), $("#regions"), 8 + 7);
    }

    function _regionsRefreshPlaceholder($this) {
        var checkedInputs = _regionsGetCheckedListJqr($this);
        var inputLabel = _buildInputLabel(checkedInputs);
        var placeholderJqr = $("#regionsTag span.msPlaceholder");
        var placeholderText = placeholderJqr.data("initial");
        if (inputLabel == '') {
            placeholderJqr.text(placeholderText);
        } else {
            placeholderJqr.text(inputLabel);
        }
    }

    function _regionsGetCheckedListJqr($this) {
        
        var thisItemJqr = $this.find("input");
        var checkedInputs =
            $("#regionsTag div.expanded input:checked:enabled").not(".not-selected-many-select-item");
        if (thisItemJqr.prop("checked")) {
            var thisItemId = thisItemJqr.attr("id");
            return checkedInputs.not("#" + thisItemId);
        } else {
            return checkedInputs.add(thisItemJqr);
        }
    }

    function _regionsChangeRegionsByDistricts(districtsList) {
        var ajaxUrl = '/epz/order/quicksearch/tagupdate.html?dtoClass=&=' + districtsList;
        $.ajax({
            url: ajaxUrl,
            dataType: 'html',
            success: function (html) {
                var containerSelector = "#regionsTagDataContainer";
                var liData = $(html).find(containerSelector + " li");
                $(containerSelector).html(liData);
                setManySelectPlaceholderText("regionsSelectBtn");
                $("#" + "regions").val("");
                _regionsDispathEvent();

                if (districtsList.length === 0) {
                    var $dataBlock = $("#regionsTagDataContainer");
                }
                $("#regionsTagDataContainer" + ' :checkbox').on('click', function () {
                    if ($dataBlock.find(':checked').size() > 5) {
                        this.checked = false;
                        alertMsBox("Возможно выбрать только 5 значений для поиска")
                    }
                });

            }
        });
    }

    function _regionsDispathEvent(e) {
        var checked = $("div.regionsExpanded input:checked");
        var outputValues = _createDropDownChecksValues(checked, 8 + 7);
        $('#searchOptionsEditContainer .regionsEventListener').each(function () {
            $(this).trigger("regionsEvent", {regionsList: outputValues});
        });
    }

    function choiceRestriction($this) {
        var $dataBlock = $("#regionsTagDataContainer");
        var checkedCount = $dataBlock.find("input[type='checkbox']:checked").not(".not-selected-many-select-item").size();
        var currentCheckBoxValue = $this.find("input[type='checkbox']").prop("checked");
        var isRegionItem = $this.find(".not-selected-many-select-item").size() == 0;
        if (checkedCount >= 5 && !currentCheckBoxValue && isRegionItem) {
            $this.find("input[type='checkbox']").prop("checked", true);
            alertMsBox("Возможно выбрать только 5 значений для поиска");
        }
    }
</script>


                

                    
                    
                    
                    






















<script type="text/javascript">
    $(document).ready(function () {
        $("#publishDateTag").on("setDefaultValues", function () {
            $("#" + "publishDateFrom").prop("value", "");
            $("#" + "publishDateTo").prop("value", "");
            $("#" + "publishDateFrom").removeClass("customInvalid");
            $("#" + "publishDateTo").removeClass("customInvalid");
            $("#threeMonthsLeft").prop("checked", false);
        });

        $("#publishDateTag input[type='text']").on("delete", function (event) {
            
                
                
                    $("#" + "publishDateTag" + " input[type='text']").val("");
                
            
        });
    });
</script>




<li id="publishDateTag" class=" ">
    <label class="vAlignTop">Дата размещения:</label>
    <div class="inlineBlock width630 errorContainer">
        <span class="padRight12">с</span>
        <input type="text" value="" name="publishDateFrom" id="publishDateFrom" class="size110 height30 datepicker_ru margRight10 hasDatepicker" title="Дата начала" placeholder="Дата начала" data-validate="{&quot;required&quot;: &quot;false&quot;, &quot;validDate&quot;: &quot;true&quot;}" data-validate_message="{&quot;validDate&quot;: &quot;Неправильная дата начала&quot;}">
        <span class="padRight12">по</span>
        <input type="text" value="" name="publishDateTo" id="publishDateTo" class="size110 height30 datepicker_ru margRight10 hasDatepicker" title="Дата окончания" placeholder="Дата окончания" data-validate="{&quot;required&quot;: &quot;false&quot;, &quot;validDate&quot;: &quot;true&quot;, &quot;validPeriod&quot;: &quot;#publishDateFrom&quot;}" data-validate_message="{&quot;validDate&quot;: &quot;Неправильная дата окончания&quot;, &quot;validPeriod&quot;: &quot;Дата начала периода должна быть меньше даты окончания периода&quot;}">

    </div>
    
</li>

                

                    
                    
                    
                    






















<script type="text/javascript">
    $(document).ready(function () {
        $("#updateDateTag").on("setDefaultValues", function () {
            $("#" + "updateDateFrom").prop("value", "");
            $("#" + "updateDateTo").prop("value", "");
            $("#" + "updateDateFrom").removeClass("customInvalid");
            $("#" + "updateDateTo").removeClass("customInvalid");
            $("#threeMonthsLeft").prop("checked", false);
        });

        $("#updateDateTag input[type='text']").on("delete", function (event) {
            
                
                
                    $("#" + "updateDateTag" + " input[type='text']").val("");
                
            
        });
    });
</script>




<li id="updateDateTag" class=" ">
    <label class="vAlignTop">Дата обновления:</label>
    <div class="inlineBlock width630 errorContainer">
        <span class="padRight12">с</span>
        <input type="text" value="" name="updateDateFrom" id="updateDateFrom" class="size110 height30 datepicker_ru margRight10 hasDatepicker" title="Дата начала" placeholder="Дата начала" data-validate="{&quot;required&quot;: &quot;false&quot;, &quot;validDate&quot;: &quot;true&quot;}" data-validate_message="{&quot;validDate&quot;: &quot;Неправильная дата начала&quot;}">
        <span class="padRight12">по</span>
        <input type="text" value="" name="updateDateTo" id="updateDateTo" class="size110 height30 datepicker_ru margRight10 hasDatepicker" title="Дата окончания" placeholder="Дата окончания" data-validate="{&quot;required&quot;: &quot;false&quot;, &quot;validDate&quot;: &quot;true&quot;, &quot;validPeriod&quot;: &quot;#updateDateFrom&quot;}" data-validate_message="{&quot;validDate&quot;: &quot;Неправильная дата окончания&quot;, &quot;validPeriod&quot;: &quot;Дата начала периода должна быть меньше даты окончания периода&quot;}">

    </div>
    
</li>

                

                    
                    
                    
                    






















<script type="text/javascript">
    $(document).ready(function () {
        $("#applSubmissionCloseDateTag").on("setDefaultValues", function () {
            $("#" + "applSubmissionCloseDateFrom").prop("value", "");
            $("#" + "applSubmissionCloseDateTo").prop("value", "");
            $("#" + "applSubmissionCloseDateFrom").removeClass("customInvalid");
            $("#" + "applSubmissionCloseDateTo").removeClass("customInvalid");
            $("#threeMonthsLeft").prop("checked", false);
        });

        $("#applSubmissionCloseDateTag input[type='text']").on("delete", function (event) {
            
                
                
                    $("#" + "applSubmissionCloseDateTag" + " input[type='text']").val("");
                
            
        });
    });
</script>




<li id="applSubmissionCloseDateTag" class=" fz44_tag fz223_tag ppRf615_tag search_tag">
    <label class="vAlignTop">Дата окончания подачи заявок:</label>
    <div class="inlineBlock width630 errorContainer">
        <span class="padRight12">с</span>
        <input type="text" value="" name="applSubmissionCloseDateFrom" id="applSubmissionCloseDateFrom" class="size110 
        height30 datepicker_ru margRight10 hasDatepicker" title="Дата начала" placeholder="Дата начала" data-validate="{
        &quot;required&quot;: &quot;false&quot;, &quot;validDate&quot;: &quot;true&quot;}" data-validate_message="{&quot
        ;validDate&quot;: &quot;Неправильная дата начала&quot;}">
        <span class="padRight12">по</span>
        <input type="text" value="" name="applSubmissionCloseDateTo" id="applSubmissionCloseDateTo" class="size110 
        height30 datepicker_ru margRight10 hasDatepicker" title="Дата окончания" placeholder="Дата окончания" data-
        validate="{&quot;required&quot;: &quot;false&quot;, &quot;validDate&quot;: &quot;true&quot;, &quot;validPeriod&
        quot;: &quot;#applSubmissionCloseDateFrom&quot;}" data-validate_message="{&quot;validDate&quot;: &quot;Неправи
        льная дата окончания&quot;, &quot;validPeriod&quot;: &quot;Дата начала периода должна быть меньше даты оконча
        ния периода&quot;}">

    </div>
    
</li>

                

                    
                    
                    
                    



















<input type="hidden" name="sortBy" value="UPDATE_DATE">


                
            </ul>
        </div>
        <div class="darkGreyBox" id="searchButtonsBlock">
            <div class="floatRight">
                <span class="clearAll" id="setDefValue"><em>Очистить все</em></span>
                <span class="bigOrangeBtn margLeft20" onclick="submitQuickSearchForm();">уточнить результаты</span>
            </div>
            
                <a href="#" onclick="saveSearchSettings()" class="saveIcon">Сохранить в настройках поиска</a>
            
        </div>
    </div>
</form>

<script type="text/javascript">
    $(document).ready(function () {
        var bannersBlockSvg = document.getElementById("bannersBlockSvg");
        var line = document.createElementNS("http://www.w3.org/2000/svg", "path");
        line.setAttribute("fill-opacity", "0");
        line.setAttribute("stroke", "#018ccd");
        line.setAttribute("stroke-width", "2");
        if (bannersBlockSvg)
            bannersBlockSvg.appendChild(line);

        if ($(".bannersMainBlock div.currentTab").parent().index() == 0) {
            // line.setAttribute("d", "M 1 75 L 1 10 C 1 10 1 1  10 1 L 200 1 C 200 1 210 1 210 10 L 210 65 C 210 65 210 75 220 75 L 910 75");
            $(".bannersMainBlock div.currentTab img").attr('src', '/epz/order/quicksearch/images/convert_open_blue.png');
        } else if ($(".bannersMainBlock div.currentTab").parent().index() == 1) {
            // line.setAttribute("d", "M 1 75 L 450 75 C 450 75 460 75  460 65 L 460 10 C 460 10 460 1 470 1 L 660 1 C 660 1 670 1 670 10 L 670 65 C 670 65 670 75 680 75 L 910 75");
            $(".bannersMainBlock div.currentTab img").attr('src', '/epz/order/quicksearch/images/calendar_check_blue.png');
        } else if ($(".bannersMainBlock div.currentTab").parent().index() == 2) {
            // line.setAttribute("d", "M 1 75 L 230 75 C 230 75 240 75  240 65 L 240 10 C 240 10 240 1 250 1 L 430 1 C 430 1 440 1 440 10 L 440 65 C 440 65 440 75 450 75 L 910 75");
            $(".bannersMainBlock div.currentTab img").attr('src', '/epz/order/quicksearch/images/bell_rings_blue.png');
        } else if ($(".bannersMainBlock div.currentTab").parent().index() == 3) {
            // line.setAttribute("d", "M 1 75 L 680 75 C 680 75 690 75  690 65 L 690 10 C 690 10 690 1 700 1 L 890 1 C 890 1 900 1 900 10 L 900 75");
            $(".bannersMainBlock div.currentTab img").attr('src', '/epz/order/quicksearch/images/shield_blue.png');
        }

        var tittleText = $("ul.tuningQuickSearchList .currentSetting").text();
        if (tittleText != "") {
            $("div.tuningQuickSearchBlock .pseudoInput").removeClass("greyText").text(tittleText);
        }
        

        var ulContainer = $("#searchOptionsViewContainer");

        if (ulContainer[0].childElementCount == 1) {
            ulContainer.append("<li><label>Параметры поиска не установлены<label/><li/>");
        }
    });

    
    drawSavedSettings("ss_", "http://zakupki.gov.ru/epz/order/quicksearch/search.html?morphology=on&pageNumber=1&sortDirection=false&recordsPerPage=_10&showLotsInfoHidden=false&fz44=on&fz223=on&af=on&ca=on&pc=on&pa=on&currencyId=-1&regionDeleted=false&sortBy=UPDATE_DATE");

    var saveQuickSearchSettingsPopup = new SaveQuickSearchSettingsPopup("/epz/order/quicksearch/",
            10,
            "saveSettingsAndClose");


    function saveSearchSettings() {
        if ($("div.tuningQuickSearchBlock .pseudoInput").hasClass("greyText")) {
            saveQuickSearchSettingsPopup.openPopup($("#savedSettingBox .tuningQuickSearchList li").length - 2);
        } else {
            $.cookie("ss_" + $("div.tuningQuickSearchBlock .pseudoInput").text(), window.location.href, {path: "/epz/order/quicksearch"});
            infoMsBox("Параметры настройки поиска обновлены");
        }
    }
    function saveSettingsAndClose(settingName) {
        if (settingName === "") {
            $(".validation-error").removeClass("hidden");
        } else {
            $(".validation-error").addClass("hidden");
            deleteHints();
            $.cookie("ss_" + settingName,
                window.location.protocol + "//" + window.location.host + window.location.pathname + "?" + $.param($('#quickSearchForm_header').serializeArray())
            );
            showHints();
            addSavedSettingOption(settingName, window.location.href, true);
        }
    }
    
</script>



    










































<script type="text/javascript">

    var timestamp;
    $(document).ready(function () {
        if ($("input#showLotsInfoHidden").val() == "true") {
            $("#expandLotsInfo").attr("checked", "checked");
            expandLots($("#expandLotsInfo"));
        }
        timestamp = new Date().getTime();

    });

    function showMsBox(msg) {
        $.msgBox({
            type: "info",
            content: msg,
            buttons: [
                {type: "cancel", value: "Ок"}
            ],
            success: function (result) {
                return true;
            }
        });
        $("div.msgBoxTitle").remove();
        $("div.msgBoxBackGround").off('click');
    }

    function downloadOrderCsv(totalCount, contextPath, criteria_csv_url, quickSearch) {
        if (totalCount > 500) {
            var submitTitle = "Продолжить";
            var cancelTitle = "Отменить";

            $.msgBox({
                type: "confirm",
                title: "<span>Сообщение</span>",
                content: "Результаты поиска превышают допустимое количество записей для выгрузки. В случае продолжения операции в файл будут выгружены первые 500 найденных записей",
                buttons: [
                    {type: "cancel", value: cancelTitle},
                    {type: "submit", value: submitTitle}
                ],
                success: function (result) {
                    if (result === submitTitle) {
                        loadOrderCsvSettings(contextPath, criteria_csv_url, quickSearch);
                    }
                }
            });
            $("div.msgBoxBackGround").off('click');
        } else {
            loadOrderCsvSettings(contextPath, criteria_csv_url, quickSearch);
        }
    }

    function loadOrderCsvSettings(contextPath, criteria_csv_url, quickSearch) {
        var params = null,
            url = null;

        if (criteria_csv_url) {
            params = criteria_csv_url + '&quickSearch=' + quickSearch;
        } else {
            params = '?quickSearch=' + quickSearch;
        }

        url = contextPath + '/orderCsvSettings/loadSettings.html' + params;
        $('.loadSettings').attr('href', url).click();
    }

    function lotInfoClick(id, el) {
        if ($("#" + id).css("display") == "none") {
            $("#" + id).slideDown(300);
            $(el).find("p").addClass("collapse");
        } else {
            $("#" + id).slideUp(300);
            $(el).find("p").removeClass("collapse");
        }
    }

    function openComplaintQuickSearch(number, isFZ94, isFZ223, isFZ44) {
        var url = "/epz/complaint/quicksearch/search_eis.html?searchString=" + number + "&strictEqual=on";
        if (isFZ94 || isFZ44) {
            url = url + "&fz94=on";
        }
        if (isFZ223) {
            url = url + "&fz223=on";
        }
        url = url + "&cancelled=on&considered=on&regarded=on";
        window.open(url);
    }

    function bankGuaranteeUrl(recordNotificationNumber) {
        var regex = /(<([^>]+)>)/ig;
        var removeXML = recordNotificationNumber.replace(regex, "");
        var url = "/epz/bankguarantee/extendedsearch/results.html?searchString=&orderNumber=" + removeXML + "&openMode=USE_DEFAULT_PARAMS";
        url += "&published=on&rejected=on&terminated=on&stopped=on&application=on&contract=on&currencyId=1";
        window.open(url);
    }

    function openContractUrl(number) {
        var url = "/epz/contract/extendedsearch/results.html?searchString=&orderNumber=" + number + "&openMode=USE_DEFAULT_PARAMS";
        url += "&fz44=on&priceFrom=0&priceTo=200000000000&contractStageList=0%2C1%2C2%2C3&budgetaryFunds=on&extraBudgetaryFunds=on";
        window.open(url);
    }
</script>

<style>
    .paginator .greyBox {
        border-radius: 0px;
        background-color: transparent;
        padding: 0px;
        display: inline-block;
     width: 65%;
    
    }

    .paginator .greyBox .paging {
        width: 100%;
    }
    
    .registerBox .greyText {
        color: #909ebb!important;
    }

    .lotsInfo table td:first-child span.greyText {
        color: #41484e !important;
    }
    .descriptTenderTd {
        padding-top: 12px;
    }
    .reportBox ul:first-child {
        margin: 0;
        padding-bottom: 4px;
        padding-top: 4px;
    }
    
</style>

<script type="text/javascript" src="/epz/order/quicksearch/js/tiny_url.js"></script>
<div class="parametrs margBtm10">
    <div class="sortBy">
        
            






<ul class="displayInlineBlock">
    <li class="displayNonePoor">Показывать по:</li>
    <li class="pageSelect"><el class="displayNoneUsual">Показывать по:</el>
        <span class=""><i>10</i></span>
        <ul>
            
                
                
                    
                        
                            <li id="_10">10</li>
                        
                    
                        
                    
                        
                            <li id="_20">20</li>
                        
                    
                        
                    
                        
                            <li id="_50">50</li>
                        
                    
                        
                    
                        
                    
                        
                    
                        
                    
                        
                    
                        
                    
                
            
        </ul>
    </li>
</ul>
        
        <ul>
            <li>Сортировать по:</li>
            
                
                <li type="UPDATE_DATE" class="sortItem activeSort ">
                    <span>Дате обновления</span>
                </li>
            
                
                <li type="PUBLISH_DATE" class="sortItem  ">
                    <span>Дате размещения</span>
                </li>
            
                
                <li type="PRICE" class="sortItem  ">
                    <span>Цене</span>
                </li>
            
                
                <li type="RELEVANCE" class="sortItem  ">
                    <span>Релевантности</span>
                </li>
            
        </ul>

        
    </div>

    <div class="paginator greyBox extendedVariant margBtm20">
        
            <a href="javascript:void(0)" class="rssBox" title="Подписаться на RSS-ленту" onclick="rssSubscribe('/epz/order/quicksearch/rss?morphology=on&amp;pageNumber=1&amp;sortDirection=false&amp;recordsPerPage=_10&amp;showLotsInfoHidden=false&amp;fz44=on&amp;fz223=on&amp;af=on&amp;ca=on&amp;pc=on&amp;pa=on&amp;currencyId=-1&amp;regionDeleted=false&amp;sortBy=UPDATE_DATE', 0)">rss</a>
        
        
            <a class="downLoad" href="#" onclick="downloadOrderCsv(25176984, '/epz/order/quicksearch', '?morphology=on&amp;pageNumber=1&amp;sortDirection=false&amp;recordsPerPage=_10&amp;showLotsInfoHidden=false&amp;fz44=on&amp;fz223=on&amp;af=on&amp;ca=on&amp;pc=on&amp;pa=on&amp;currencyId=-1&amp;regionDeleted=false&amp;sortBy=UPDATE_DATE', 'true')" title="Выгрузить результаты поиска"></a>
            <a class="loadSettings linkPopUp" href="#"></a>
        

        

        














    



    <div class="paginator greyBox "> 
        
            
                
                
                    
                    




<p class="allRecords">





    Всего записей: более <strong>25&nbsp;000&nbsp;000</strong><!-- total: 25 176 984-->
    
</p>
                
            
            
                
                    






















    




    
        
        
    
    



    



    
    
        
    


<ul class="pages">
    

    

    
    

    
    

        

        

        

        

        

        
    


    <li class="page">
        <a class="page__link page__link_active">
            <span class="link-text">1</span>
        </a>
    </li>


    
    

        

        
            
                
                    <li class="page">
                        <a href="javascript:goToPage(2)" data-pagenumber="2" class="page__link">
                            <span class="link-text">2</span>
                        </a>
                    </li>
                
                
            
        

        

        
            
                
                    <li class="page">
                        <a href="javascript:goToPage(3)" data-pagenumber="3" class="page__link">
                            <span class="link-text">3</span>
                        </a>
                    </li>
                
                
            
        

        
        
            <li class="page">
                <span class="link-text-enum">...</span>
            </li>
        
        

        

        
            
                
                    <li class="page">
                        <a href="javascript:goToPage(100)" data-pagenumber="100" class="page__link">
                            <span class="link-text">100</span>
                        </a>
                    </li>
                
                
            
        
    

    
    

    

    
        
            
                <a href="javascript:goToPage(2)" data-pagenumber="2" class="paginator-button paginator-button-next"><img src="/epz/order/quicksearch/img/icons/arrow-prime.svg" alt=""></a>
            
            
        
    
</ul>

                    
                
                
            
        
        

    </div>




        
            <label class="customCheckbox floatLeft">
                <input style="margin-top: 0px !important;" id="expandLotsInfo" type="checkbox">
                <label style="padding-top: 0px !important;" for="expandLotsInfo">Развернуть информацию о лотах</label>
            </label>
        
        <div class="clear"></div>
    </div>
    
    
        
        
        
        
        
        
        
        
        
        
        
        

        
        
        
        
        
        
        
        
        
        
        
        
        



        
        
        
        

        <div class="registerBox registerBoxBank margBtm20">
            
            
                
                    <div class="boxIcons">
                    
                        
                        
                            <a href="http://zakupki.gov.ru/223/purchase/public/download/signs/render-pf.html?id=36811894&amp;modal=true" class="cryptoSignLink newExternalPopUpLink pWidth_840" shablon-pattern="223FZ"></a>
                        
                    
                        
                            
                            
                                <a href="http://zakupki.gov.ru/223/purchase/public/notification/print-form/show.html?noticeId=8347436" target="_blank" class="printLink"></a>
                            
                        
                    </div>
                
            
            <table cellspacing="0" cellpadding="0">
                <tbody><tr>
                    <td class="tenderTd" style=" width: 26%">
                        <dl>
                            
                            <dt>
                                <strong>
                                    
                                        
                                        
                                            Конкурс в электронной форме
                                        
                                    
                                </strong>
                            </dt>
                            <dd>
                                    
                                
                            </dd>
                            <dt>
                                
                                    
                                        
                                            
                                                <span class="fzNews noWrap">Подача заявок /
                                                    
                                                    <span class="orange">223-ФЗ</span></span>
                                            
                                            
                                            
                                            
                                            
                                        
                                    
                                    
                                
                            </dt>
                            
                            <dd>
                                
                                    <span class="greyText">Начальная цена</span><br>
                                    <strong>
                                        

                                        3&nbsp;500&nbsp;000
                                        <span class="fractionNumber">,00</span>
                                    </strong><br><span class="currency">Российский рубль</span>
                                
                            </dd>
                            <dd>
                                
                            </dd>
                        </dl>
                    </td>

                    <td class="descriptTenderTd">
                        <dl>
                            <dt>
                                <a target="_blank" href="http://zakupki.gov.ru/223/purchase/public/purchase/info/common-info.html?regNumber=31908086191">
                                    № 31908086191
                                </a>
                                    
                                    
                                
                            </dt>
                            <dd class="nameOrganization">
                                
                                    
                                    
                                        
                                        
                                        
                                            Заказчик:
                                        
                                        
                                            
                                                
                                            
                                            
                                        
                                        <ul>
                                            <li>
                                                <a target="_blank" href="http://zakupki.gov.ru/223/ppa/public/organization/organization.html?epz=true&amp;style44=false&amp;agencyId=1016" onclick="window.open(this.href); return false;">
                                                    АКЦИОНЕРНОЕ ОБЩЕСТВО "ЮЖНЫЕ ЭЛЕКТРИЧЕСКИЕ СЕТИ КАМЧАТКИ"
                                                </a>
                                            </li>
                                        </ul>
                                    
                                    
                                
                            </dd>
                            <dd>
                                Право заключения договора на поставку кабеля силового с изоляцией из сшитого полиэтилена (СПЭ) для нужд АО «ЮЭСК»
                                <ul></ul>
                            </dd>
                            
                            
                            
                        </dl>
                    </td>

                    <td class="amountTenderTd">
                        <ul>
                            <li><label>Размещено:</label> 11.07.2019</li>
                            <li><label>Обновлено:</label> 05.08.2019</li>
                        </ul>
                    </td>
                </tr>
                
            </tbody></table>
            <div class="reportBox">
                <ul>
                    <ul>
                            
                        <li><a href="http://zakupki.gov.ru/223/purchase/public/purchase/info/common-info.html?regNumber=31908086191" target="_blank">
                            Сведения</a>
                        </li>

                            
                        <li>
                            <a href="http://zakupki.gov.ru/223/purchase/public/purchase/info/documents.html?regNumber=31908086191" target="_blank">
                            Документы</a>
                        </li>

                            
                        
                            <li><a href="http://zakupki.gov.ru/223/purchase/public/purchase/info/changes-and-clarifications.html?regNumber=31908086191" target="_blank">
                                Изменения и разъяснения</a>
                            </li>
                        

                        
                            
                            <li><a onclick="openComplaintQuickSearch('31908086191', false, true, false)" style="cursor: pointer;">
                                Жалобы</a>
                            </li>
                        


                        
                            
                            
                            
                            
                        

                            
                            
                            
                        

                            
                            
                        

                            
                        
                        
                        
                    </ul>
                </ul>
            </div>
        </div>
    
        
        
        
        
        
        
        
        
        
        
        
        

        
        
        
        
        
        
        
        
        
        
        
        
        



        
        
        
        

        <div class="registerBox registerBoxBank margBtm20">
            
            
                
                    <div class="boxIcons">
                    
                        

                            <a href="/epz/order/notice/printForm/list.html?regNumber=0838300001219000004" class="cryptoSignLink linkPopUp pWidth_840">
                            </a>
                        
                        
                    
                        
                            
                                <a href="/epz/order/notice/printForm/view.html?regNumber=0838300001219000004" target="_blank" class="printLink"></a>
                            
                            
                        
                    </div>
                
            
            <table cellspacing="0" cellpadding="0">
                <tbody><tr>
                    <td class="tenderTd" style=" width: 26%">
                        <dl>
                            
                            <dt>
                                <strong>
                                    
                                        
                                        
                                            Электронный аукцион
                                        
                                    
                                </strong>
                            </dt>
                            <dd>
                                    
                                
                            </dd>
                            <dt>
                                
                                    
                                        
                                            
                                            
                                            
                                            
                                            <span class="checked noWrap">
                                                                            
                                                                            Процедура завершена /
                                                                            
                                                                        
                                                    
                                                    <span class="orange">44-ФЗ</span></span>
                                            
                                            
                                        
                                    
                                    
                                
                            </dt>
                            
                            <dd>
                                
                                    <span class="greyText">Начальная цена</span><br>
                                    <strong>
                                        

                                        11&nbsp;533&nbsp;590
                                        <span class="fractionNumber">,00</span>
                                    </strong><br><span class="currency">Российский рубль</span>
                                
                            </dd>
                            <dd>
                                
                            </dd>
                        </dl>
                    </td>

                    <td class="descriptTenderTd">
                        <dl>
                            <dt>
                                <a target="_blank" href="/epz/order/notice/ea44/view/common-info.html?regNumber=0838300001219000004">
                                    № 0838300001219000004
                                </a>
                                    
                                    
                                
                            </dt>
                            <dd class="nameOrganization">
                                
                                    
                                    
                                    
                                        
                                            
                                            
                                                Заказчик:
                                                <ul>
                                                    <li>
                                                        
                                                            
                                                                
                                                                    <a target="_blank" href="/epz/organization/view/info.html?organizationId=1901708" onclick="window.open(this.href); return false;">
                                                                        ОТДЕЛ ПО УПРАВЛЕНИЮ ЖИЛИЩНО-КОММУНАЛЬНЫМ ХОЗЯЙСТВОМ АДМИНИСТРАЦИИ КОРЯКСКОГО СЕЛЬСКОГО ПОСЕЛЕНИЯ - МУНИЦИПАЛЬНОЕ КАЗЕННОЕ УЧРЕЖДЕНИЕ
                                                                    </a>
                                                                
                                                            
                                                            
                                                        
                                                    </li>
                                                </ul>
                                            
                                        
                                    
                                
                            </dd>
                            <dd>
                                Выполнение работ по складированию скального грунта с целью предупреждения чрезвычайных ситуаций на территории Корякского сельского поселения
                                <ul></ul>
                            </dd>
                            
                                <dd class="padTop10">
                                    Идентификационный код закупки(ИКЗ):
                                    <dl class="greyText margTop0 padTop8">
                                        









    193410504257341050100100060014312244



                                    </dl>
                                </dd>
                            
                            
                            
                        </dl>
                    </td>

                    <td class="amountTenderTd">
                        <ul>
                            <li><label>Размещено:</label> 23.07.2019</li>
                            <li><label>Обновлено:</label> 05.08.2019</li>
                        </ul>
                    </td>
                </tr>
                
            </tbody></table>
            <div class="reportBox">
                <ul>
                    <ul>
                            
                        <li><a href="/epz/order/notice/ea44/view/common-info.html?regNumber=0838300001219000004" target="_blank">
                            Сведения</a>
                        </li>

                            
                        <li>
                            <a href="/epz/order/notice/ea44/view/documents.html?regNumber=0838300001219000004" target="_blank">
                            Документы</a>
                        </li>

                            
                        

                        
                            
                            <li><a onclick="openComplaintQuickSearch('0838300001219000004', false, false, true)" style="cursor: pointer;">
                                Жалобы</a>
                            </li>
                        


                        
                            
                            
                            
                            
                        

                            
                            
                            
                        

                            
                            
                        
                            <li><a onclick="openContractUrl('0838300001219000004')" style="cursor: pointer;">
                                Контракты</a>
                            </li>
                        

                            
                        
                        
                            <li><a onclick="bankGuaranteeUrl('0838300001219000004')" style="cursor: pointer;">
                                Банковские гарантии</a>
                            </li>
                        
                        
                    </ul>
                </ul>
            </div>
        </div>
    
        
        
        
        
        
        
        
        
        
        
        
        

        
        
        
        
        
        
        
        
        
        
        
        
        



        
        
        
        

        <div class="registerBox registerBoxBank margBtm20">
            
            
                
                    <div class="boxIcons">
                    
                        

                            <a href="/epz/order/notice/printForm/list.html?regNumber=0138300016019000005" class="cryptoSignLink linkPopUp pWidth_840">
                            </a>
                        
                        
                    
                        
                            
                                <a href="/epz/order/notice/printForm/view.html?regNumber=0138300016019000005" target="_blank" class="printLink"></a>
                            
                            
                        
                    </div>
                
            
            <table cellspacing="0" cellpadding="0">
                <tbody><tr>
                    <td class="tenderTd" style=" width: 26%">
                        <dl>
                            
                            <dt>
                                <strong>
                                    
                                        
                                        
                                            Электронный аукцион
                                        
                                    
                                </strong>
                            </dt>
                            <dd>
                                    
                                
                            </dd>
                            <dt>
                                
                                    
                                        
                                            
                                            
                                            
                                                <span class="blockIco noWrap">Процедура отменена /
                                                    
                                                    <span class="orange">44-ФЗ</span></span>
                                            
                                            
                                            
                                        
                                    
                                    
                                
                            </dt>
                            
                            <dd>
                                
                                    <span class="greyText">Начальная цена</span><br>
                                    <strong>
                                        

                                        6&nbsp;000&nbsp;000
                                        <span class="fractionNumber">,00</span>
                                    </strong><br><span class="currency">Российский рубль</span>
                                
                            </dd>
                            <dd>
                                
                            </dd>
                        </dl>
                    </td>

                    <td class="descriptTenderTd">
                        <dl>
                            <dt>
                                <a target="_blank" href="/epz/order/notice/ea44/view/common-info.html?regNumber=0138300016019000005">
                                    № 0138300016019000005
                                </a>
                                    
                                    
                                
                            </dt>
                            <dd class="nameOrganization">
                                
                                    
                                    
                                    
                                        
                                            
                                            
                                                Заказчик:
                                                <ul>
                                                    <li>
                                                        
                                                            
                                                                
                                                                    <a target="_blank" href="/epz/organization/view/info.html?organizationId=1168542" onclick="window.open(this.href); return false;">
                                                                        АДМИНИСТРАЦИЯ КРУТОГОРОВСКОГО СЕЛЬСКОГО ПОСЕЛЕНИЯ СОБОЛЕВСКОГО МУНИЦИПАЛЬНОГО РАЙОНА КАМЧАТСКОГО КРАЯ
                                                                    </a>
                                                                
                                                            
                                                            
                                                        
                                                    </li>
                                                </ul>
                                            
                                        
                                    
                                
                            </dd>
                            <dd>
                                Поставка снегоболотохода
                                <ul></ul>
                            </dd>
                            
                                <dd class="padTop10">
                                    Идентификационный код закупки(ИКЗ):
                                    <dl class="greyText margTop0 padTop8">
                                        









    193410700172741070100100120012910244



                                    </dl>
                                </dd>
                            
                            
                            
                        </dl>
                    </td>

                    <td class="amountTenderTd">
                        <ul>
                            <li><label>Размещено:</label> 25.07.2019</li>
                            <li><label>Обновлено:</label> 05.08.2019</li>
                        </ul>
                    </td>
                </tr>
                
            </tbody></table>
            <div class="reportBox">
                <ul>
                    <ul>
                            
                        <li><a href="/epz/order/notice/ea44/view/common-info.html?regNumber=0138300016019000005" target="_blank">
                            Сведения</a>
                        </li>

                            
                        <li>
                            <a href="/epz/order/notice/ea44/view/documents.html?regNumber=0138300016019000005" target="_blank">
                            Документы</a>
                        </li>

                            
                        

                        
                            
                            <li><a onclick="openComplaintQuickSearch('0138300016019000005', false, false, true)" style="cursor: pointer;">
                                Жалобы</a>
                            </li>
                        


                        
                            
                            
                            
                            
                        

                            
                            
                            
                        

                            
                            
                        
                            <li><a onclick="openContractUrl('0138300016019000005')" style="cursor: pointer;">
                                Контракты</a>
                            </li>
                        

                            
                        
                        
                            <li><a onclick="bankGuaranteeUrl('0138300016019000005')" style="cursor: pointer;">
                                Банковские гарантии</a>
                            </li>
                        
                        
                    </ul>
                </ul>
            </div>
        </div>
    
        
        
        
        
        
        
        
        
        
        
        
        

        
        
        
        
        
        
        
        
        
        
        
        
        



        
        
        
        

        <div class="registerBox registerBoxBank margBtm20">
            
            
                
                    <div class="boxIcons">
                    
                        
                        
                            <a href="http://zakupki.gov.ru/223/purchase/public/download/signs/render-pf.html?id=36808051&amp;modal=true" class="cryptoSignLink newExternalPopUpLink pWidth_840" shablon-pattern="223FZ"></a>
                        
                    
                        
                            
                            
                                <a href="http://zakupki.gov.ru/223/purchase/public/notification/print-form/show.html?noticeId=8371724" target="_blank" class="printLink"></a>
                            
                        
                    </div>
                
            
            <table cellspacing="0" cellpadding="0">
                <tbody><tr>
                    <td class="tenderTd" style=" width: 26%">
                        <dl>
                            
                            <dt>
                                <strong>
                                    
                                        
                                        
                                            Запрос предложений в электронной форме
                                        
                                    
                                </strong>
                            </dt>
                            <dd>
                                    
                                
                            </dd>
                            <dt>
                                
                                    
                                        
                                            
                                            
                                                <span class="timeNews noWrap">
                                                    Работа комиссии /
                                                    
                                                    <span class="orange
                                                         padLeft20 ">223-ФЗ</span></span>
                                            
                                            
                                            
                                            
                                        
                                    
                                    
                                
                            </dt>
                            
                            <dd>
                                
                                    <span class="greyText">Начальная цена</span><br>
                                    <strong>
                                        

                                        10&nbsp;304&nbsp;900
                                        <span class="fractionNumber">,00</span>
                                    </strong><br><span class="currency">Российский рубль</span>
                                
                            </dd>
                            <dd>
                                
                            </dd>
                        </dl>
                    </td>

                    <td class="descriptTenderTd">
                        <dl>
                            <dt>
                                <a target="_blank" href="http://zakupki.gov.ru/223/purchase/public/purchase/info/common-info.html?regNumber=31908109600">
                                    № 31908109600
                                </a>
                                    
                                    
                                
                            </dt>
                            <dd class="nameOrganization">
                                
                                    
                                    
                                        
                                        
                                        
                                            Заказчик:
                                        
                                        
                                            
                                                
                                            
                                            
                                        
                                        <ul>
                                            <li>
                                                <a target="_blank" href="http://zakupki.gov.ru/223/ppa/public/organization/organization.html?epz=true&amp;style44=false&amp;agencyId=4862" onclick="window.open(this.href); return false;">
                                                    АКЦИОНЕРНОЕ ОБЩЕСТВО "ГЕОТЕРМ"
                                                </a>
                                            </li>
                                        </ul>
                                    
                                    
                                
                            </dd>
                            <dd>
                                0005-РЕМ-РЕМ ПРОД-2019-Геотерм «Разработка проектной и рабочей документации на капитальный ремонт мостов»
                                <ul></ul>
                            </dd>
                            
                            
                            
                        </dl>
                    </td>

                    <td class="amountTenderTd">
                        <ul>
                            <li><label>Размещено:</label> 18.07.2019</li>
                            <li><label>Обновлено:</label> 05.08.2019</li>
                        </ul>
                    </td>
                </tr>
                
            </tbody></table>
            <div class="reportBox">
                <ul>
                    <ul>
                            
                        <li><a href="http://zakupki.gov.ru/223/purchase/public/purchase/info/common-info.html?regNumber=31908109600" target="_blank">
                            Сведения</a>
                        </li>

                            
                        <li>
                            <a href="http://zakupki.gov.ru/223/purchase/public/purchase/info/documents.html?regNumber=31908109600" target="_blank">
                            Документы</a>
                        </li>

                            
                        
                            <li><a href="http://zakupki.gov.ru/223/purchase/public/purchase/info/changes-and-clarifications.html?regNumber=31908109600" target="_blank">
                                Изменения и разъяснения</a>
                            </li>
                        

                        
                            
                            <li><a onclick="openComplaintQuickSearch('31908109600', false, true, false)" style="cursor: pointer;">
                                Жалобы</a>
                            </li>
                        


                        
                            
                            
                            
                            
                        
                            <li>
                                
                                    
                                        <a href="http://zakupki.gov.ru/223/purchase/public/purchase/info/protocols.html?regNumber=31908109600" target="_blank">
                                    
                                    
                                
                                Протоколы</a>
                            </li>
                        

                            
                            
                            
                        

                            
                            
                        

                            
                        
                        
                        
                    </ul>
                </ul>
            </div>
        </div>
    
        
        
        
        
        
        
        
        
        
        
        
        

        
        
        
        
        
        
        
        
        
        
        
        
        



        
        
        
        

        <div class="registerBox registerBoxBank margBtm20">
            
            
                
                    <div class="boxIcons">
                    
                        
                        
                            <a href="http://zakupki.gov.ru/223/purchase/public/download/signs/render-pf.html?id=36601354&amp;modal=true" class="cryptoSignLink newExternalPopUpLink pWidth_840" shablon-pattern="223FZ"></a>
                        
                    
                        
                            
                            
                                <a href="http://zakupki.gov.ru/223/purchase/public/notification/print-form/show.html?noticeId=8362089" target="_blank" class="printLink"></a>
                            
                        
                    </div>
                
            
            <table cellspacing="0" cellpadding="0">
                <tbody><tr>
                    <td class="tenderTd" style=" width: 26%">
                        <dl>
                            
                            <dt>
                                <strong>
                                    
                                        
                                        
                                            Конкурс в электронной форме
                                        
                                    
                                </strong>
                            </dt>
                            <dd>
                                    
                                
                            </dd>
                            <dt>
                                
                                    
                                        
                                            
                                            
                                                <span class="timeNews noWrap">
                                                    Работа комиссии /
                                                    
                                                    <span class="orange
                                                         padLeft20 ">223-ФЗ</span></span>
                                            
                                            
                                            
                                            
                                        
                                    
                                    
                                
                            </dt>
                            
                            <dd>
                                
                                    <span class="greyText">Начальная цена</span><br>
                                    <strong>
                                        

                                        18&nbsp;506&nbsp;773
                                        <span class="fractionNumber">,62</span>
                                    </strong><br><span class="currency">Российский рубль</span>
                                
                            </dd>
                            <dd>
                                
                            </dd>
                        </dl>
                    </td>

                    <td class="descriptTenderTd">
                        <dl>
                            <dt>
                                <a target="_blank" href="http://zakupki.gov.ru/223/purchase/public/purchase/info/common-info.html?regNumber=31908100365">
                                    № 31908100365
                                </a>
                                    
                                    
                                
                            </dt>
                            <dd class="nameOrganization">
                                
                                    
                                    
                                        
                                        
                                        
                                            Заказчик:
                                        
                                        
                                            
                                                
                                            
                                            
                                        
                                        <ul>
                                            <li>
                                                <a target="_blank" href="http://zakupki.gov.ru/223/ppa/public/organization/organization.html?epz=true&amp;style44=false&amp;agencyId=2335" onclick="window.open(this.href); return false;">
                                                    ПУБЛИЧНОЕ АКЦИОНЕРНОЕ ОБЩЕСТВО ЭНЕРГЕТИКИ И ЭЛЕКТРИФИКАЦИИ "САХАЛИНЭНЕРГО"
                                                </a>
                                            </li>
                                        </ul>
                                    
                                    
                                
                            </dd>
                            <dd>
                                Право заключения договора на поставку опор металлических для ВЛ 35кВ
                                <ul></ul>
                            </dd>
                            
                            
                            
                        </dl>
                    </td>

                    <td class="amountTenderTd">
                        <ul>
                            <li><label>Размещено:</label> 16.07.2019</li>
                            <li><label>Обновлено:</label> 05.08.2019</li>
                        </ul>
                    </td>
                </tr>
                
            </tbody></table>
            <div class="reportBox">
                <ul>
                    <ul>
                            
                        <li><a href="http://zakupki.gov.ru/223/purchase/public/purchase/info/common-info.html?regNumber=31908100365" target="_blank">
                            Сведения</a>
                        </li>

                            
                        <li>
                            <a href="http://zakupki.gov.ru/223/purchase/public/purchase/info/documents.html?regNumber=31908100365" target="_blank">
                            Документы</a>
                        </li>

                            
                        
                            <li><a href="http://zakupki.gov.ru/223/purchase/public/purchase/info/changes-and-clarifications.html?regNumber=31908100365" target="_blank">
                                Изменения и разъяснения</a>
                            </li>
                        

                        
                            
                            <li><a onclick="openComplaintQuickSearch('31908100365', false, true, false)" style="cursor: pointer;">
                                Жалобы</a>
                            </li>
                        


                        
                            
                            
                            
                            
                        

                            
                            
                            
                        

                            
                            
                        

                            
                        
                        
                        
                    </ul>
                </ul>
            </div>
        </div>
    
        
        
        
        
        
        
        
        
        
        
        
        

        
        
        
        
        
        
        
        
        
        
        
        
        



        
        
        
        

        <div class="registerBox registerBoxBank margBtm20">
            
            
                
                    <div class="boxIcons">
                    
                        
                        
                            <a href="http://zakupki.gov.ru/223/purchase/public/download/signs/render-pf.html?id=36701308&amp;modal=true" class="cryptoSignLink newExternalPopUpLink pWidth_840" shablon-pattern="223FZ"></a>
                        
                    
                        
                            
                            
                                <a href="http://zakupki.gov.ru/223/purchase/public/notification/print-form/show.html?noticeId=8406548" target="_blank" class="printLink"></a>
                            
                        
                    </div>
                
            
            <table cellspacing="0" cellpadding="0">
                <tbody><tr>
                    <td class="tenderTd" style=" width: 26%">
                        <dl>
                            
                            <dt>
                                <strong>
                                    
                                        
                                        
                                            Закупка у единственного поставщика (подрядчика, исполнителя) (до 01.07.18)
                                        
                                    
                                </strong>
                            </dt>
                            <dd>
                                    
                                
                            </dd>
                            <dt>
                                
                                    
                                        
                                            
                                            
                                            
                                                <span class="blockIco noWrap">Процедура отменена /
                                                    
                                                    <span class="orange">223-ФЗ</span></span>
                                            
                                            
                                            
                                        
                                    
                                    
                                
                            </dt>
                            
                            <dd>
                                
                                    <span class="greyText">Начальная цена</span><br>
                                    <strong>
                                        

                                        25&nbsp;228&nbsp;548
                                        <span class="fractionNumber">,34</span>
                                    </strong><br><span class="currency">Российский рубль</span>
                                
                            </dd>
                            <dd>
                                
                            </dd>
                        </dl>
                    </td>

                    <td class="descriptTenderTd">
                        <dl>
                            <dt>
                                <a target="_blank" href="http://zakupki.gov.ru/223/purchase/public/purchase/info/common-info.html?regNumber=31908143333">
                                    № 31908143333
                                </a>
                                    
                                    
                                
                            </dt>
                            <dd class="nameOrganization">
                                
                                    
                                    
                                        
                                        
                                        
                                            Заказчик:
                                        
                                        
                                            
                                                
                                            
                                            
                                        
                                        <ul>
                                            <li>
                                                <a target="_blank" href="http://zakupki.gov.ru/223/ppa/public/organization/organization.html?epz=true&amp;style44=false&amp;agencyId=10502" onclick="window.open(this.href); return false;">
                                                    Охинское государственное унитарное дорожное предприятие Сахалинской области
                                                </a>
                                            </li>
                                        </ul>
                                    
                                    
                                
                            </dd>
                            <dd>
                                оказание услуг финансовой аренды (лизинга)
                                <ul></ul>
                            </dd>
                            
                            
                            
                        </dl>
                    </td>

                    <td class="amountTenderTd">
                        <ul>
                            <li><label>Размещено:</label> 29.07.2019</li>
                            <li><label>Обновлено:</label> 05.08.2019</li>
                        </ul>
                    </td>
                </tr>
                
            </tbody></table>
            <div class="reportBox">
                <ul>
                    <ul>
                            
                        <li><a href="http://zakupki.gov.ru/223/purchase/public/purchase/info/common-info.html?regNumber=31908143333" target="_blank">
                            Сведения</a>
                        </li>

                            
                        <li>
                            <a href="http://zakupki.gov.ru/223/purchase/public/purchase/info/documents.html?regNumber=31908143333" target="_blank">
                            Документы</a>
                        </li>

                            
                        
                            <li><a href="http://zakupki.gov.ru/223/purchase/public/purchase/info/changes-and-clarifications.html?regNumber=31908143333" target="_blank">
                                Изменения и разъяснения</a>
                            </li>
                        

                        
                            
                            <li><a onclick="openComplaintQuickSearch('31908143333', false, true, false)" style="cursor: pointer;">
                                Жалобы</a>
                            </li>
                        


                        
                            
                            
                            
                            
                        
                            <li>
                                
                                    
                                        <a href="http://zakupki.gov.ru/223/purchase/public/purchase/info/protocols.html?regNumber=31908143333" target="_blank">
                                    
                                    
                                
                                Протоколы</a>
                            </li>
                        

                            
                            
                            
                        

                            
                            
                        

                            
                        
                        
                        
                    </ul>
                </ul>
            </div>
        </div>
    
        
        
        
        
        
        
        
        
        
        
        
        

        
        
        
        
        
        
        
        
        
        
        
        
        



        
        
        
        

        <div class="registerBox registerBoxBank margBtm20">
            
            
                
                    <div class="boxIcons">
                    
                        

                            <a href="/epz/order/notice/printForm/list.html?regNumber=0338300004619000095" class="cryptoSignLink linkPopUp pWidth_840">
                            </a>
                        
                        
                    
                        
                            
                                <a href="/epz/order/notice/printForm/view.html?regNumber=0338300004619000095" target="_blank" class="printLink"></a>
                            
                            
                        
                    </div>
                
            
            <table cellspacing="0" cellpadding="0">
                <tbody><tr>
                    <td class="tenderTd" style=" width: 26%">
                        <dl>
                            
                            <dt>
                                <strong>
                                    
                                        
                                        
                                            Электронный аукцион
                                        
                                    
                                </strong>
                            </dt>
                            <dd>
                                    
                                
                            </dd>
                            <dt>
                                
                                    
                                        
                                            
                                            
                                                <span class="timeNews noWrap">
                                                    Работа комиссии /
                                                    
                                                    <span class="orange
                                                        ">44-ФЗ</span></span>
                                            
                                            
                                            
                                            
                                        
                                    
                                    
                                
                            </dt>
                            
                            <dd>
                                
                                    <span class="greyText">Начальная цена</span><br>
                                    <strong>
                                        

                                        5&nbsp;803&nbsp;100
                                        <span class="fractionNumber">,40</span>
                                    </strong><br><span class="currency">Российский рубль</span>
                                
                            </dd>
                            <dd>
                                
                            </dd>
                        </dl>
                    </td>

                    <td class="descriptTenderTd">
                        <dl>
                            <dt>
                                <a target="_blank" href="/epz/order/notice/ea44/view/common-info.html?regNumber=0338300004619000095">
                                    № 0338300004619000095
                                </a>
                                    
                                    
                                
                            </dt>
                            <dd class="nameOrganization">
                                
                                    
                                    
                                    
                                        
                                            
                                            
                                                Заказчик:
                                                <ul>
                                                    <li>
                                                        
                                                            
                                                                
                                                                    <a target="_blank" href="/epz/organization/view/info.html?organizationId=668884" onclick="window.open(this.href); return false;">
                                                                        ГОСУДАРСТВЕННОЕ БЮДЖЕТНОЕ УЧРЕЖДЕНИЕ ЗДРАВООХРАНЕНИЯ КАМЧАТСКОГО КРАЯ "ПЕТРОПАВЛОВСК-КАМЧАТСКАЯ ГОРОДСКАЯ БОЛЬНИЦА № 1"
                                                                    </a>
                                                                
                                                            
                                                            
                                                        
                                                    </li>
                                                </ul>
                                            
                                        
                                    
                                
                            </dd>
                            <dd>
                                Выполнение подрядных работ по капитальному ремонту кровли поликлиники
                                <ul></ul>
                            </dd>
                            
                                <dd class="padTop10">
                                    Идентификационный код закупки(ИКЗ):
                                    <dl class="greyText margTop0 padTop8">
                                        









    192410102924341010100100030010000000



                                    </dl>
                                </dd>
                            
                            
                            
                        </dl>
                    </td>

                    <td class="amountTenderTd">
                        <ul>
                            <li><label>Размещено:</label> 09.07.2019</li>
                            <li><label>Обновлено:</label> 05.08.2019</li>
                        </ul>
                    </td>
                </tr>
                
            </tbody></table>
            <div class="reportBox">
                <ul>
                    <ul>
                            
                        <li><a href="/epz/order/notice/ea44/view/common-info.html?regNumber=0338300004619000095" target="_blank">
                            Сведения</a>
                        </li>

                            
                        <li>
                            <a href="/epz/order/notice/ea44/view/documents.html?regNumber=0338300004619000095" target="_blank">
                            Документы</a>
                        </li>

                            
                        

                        
                            
                            <li><a onclick="openComplaintQuickSearch('0338300004619000095', false, false, true)" style="cursor: pointer;">
                                Жалобы</a>
                            </li>
                        


                        
                            
                            
                            
                            
                        

                            
                            
                            
                        

                            
                            
                        

                            
                        
                        
                            <li><a onclick="bankGuaranteeUrl('0338300004619000095')" style="cursor: pointer;">
                                Банковские гарантии</a>
                            </li>
                        
                        
                    </ul>
                </ul>
            </div>
        </div>
    
        
        
        
        
        
        
        
        
        
        
        
        

        
        
        
        
        
        
        
        
        
        
        
        
        



        
        
        
        

        <div class="registerBox registerBoxBank margBtm20">
            
            
                
                    <div class="boxIcons">
                    
                        

                            <a href="/epz/order/notice/printForm/list.html?regNumber=0361300010719000055" class="cryptoSignLink linkPopUp pWidth_840">
                            </a>
                        
                        
                    
                        
                            
                                <a href="/epz/order/notice/printForm/view.html?regNumber=0361300010719000055" target="_blank" class="printLink"></a>
                            
                            
                        
                    </div>
                
            
            <table cellspacing="0" cellpadding="0">
                <tbody><tr>
                    <td class="tenderTd" style=" width: 26%">
                        <dl>
                            
                            <dt>
                                <strong>
                                    
                                        
                                        
                                            Электронный аукцион
                                        
                                    
                                </strong>
                            </dt>
                            <dd>
                                    
                                
                            </dd>
                            <dt>
                                
                                    
                                        
                                            
                                            
                                            
                                            
                                            <span class="checked noWrap">
                                                                            
                                                                            Процедура завершена /
                                                                            
                                                                        
                                                    
                                                    <span class="orange">44-ФЗ</span></span>
                                            
                                            
                                        
                                    
                                    
                                
                            </dt>
                            
                            <dd>
                                
                                    <span class="greyText">Начальная цена</span><br>
                                    <strong>
                                        

                                        39&nbsp;524&nbsp;106
                                        <span class="fractionNumber">,00</span>
                                    </strong><br><span class="currency">Российский рубль</span>
                                
                            </dd>
                            <dd>
                                
                            </dd>
                        </dl>
                    </td>

                    <td class="descriptTenderTd">
                        <dl>
                            <dt>
                                <a target="_blank" href="/epz/order/notice/ea44/view/common-info.html?regNumber=0361300010719000055">
                                    № 0361300010719000055
                                </a>
                                    
                                    
                                
                            </dt>
                            <dd class="nameOrganization">
                                
                                    
                                    
                                    
                                        
                                            
                                            
                                                Заказчик:
                                                <ul>
                                                    <li>
                                                        
                                                            
                                                                
                                                                    <a target="_blank" href="/epz/organization/view/info.html?organizationId=763934" onclick="window.open(this.href); return false;">
                                                                        АДМИНИСТРАЦИЯ МУНИЦИПАЛЬНОГО ОБРАЗОВАНИЯ "КУРИЛЬСКИЙ ГОРОДСКОЙ ОКРУГ"
                                                                    </a>
                                                                
                                                            
                                                            
                                                        
                                                    </li>
                                                </ul>
                                            
                                        
                                    
                                
                            </dd>
                            <dd>
                                Ремонт автомобильных дорог муниципального образования "Курильский городской округ"
                                <ul></ul>
                            </dd>
                            
                                <dd class="padTop10">
                                    Идентификационный код закупки(ИКЗ):
                                    <dl class="greyText margTop0 padTop8">
                                        









    193651100223165110100100370044211243



                                    </dl>
                                </dd>
                            
                            
                            
                        </dl>
                    </td>

                    <td class="amountTenderTd">
                        <ul>
                            <li><label>Размещено:</label> 25.07.2019</li>
                            <li><label>Обновлено:</label> 05.08.2019</li>
                        </ul>
                    </td>
                </tr>
                
            </tbody></table>
            <div class="reportBox">
                <ul>
                    <ul>
                            
                        <li><a href="/epz/order/notice/ea44/view/common-info.html?regNumber=0361300010719000055" target="_blank">
                            Сведения</a>
                        </li>

                            
                        <li>
                            <a href="/epz/order/notice/ea44/view/documents.html?regNumber=0361300010719000055" target="_blank">
                            Документы</a>
                        </li>

                            
                        

                        
                            
                            <li><a onclick="openComplaintQuickSearch('0361300010719000055', false, false, true)" style="cursor: pointer;">
                                Жалобы</a>
                            </li>
                        


                        
                            
                            
                            
                            
                        

                            
                            
                            
                        

                            
                            
                        
                            <li><a onclick="openContractUrl('0361300010719000055')" style="cursor: pointer;">
                                Контракты</a>
                            </li>
                        

                            
                        
                        
                            <li><a onclick="bankGuaranteeUrl('0361300010719000055')" style="cursor: pointer;">
                                Банковские гарантии</a>
                            </li>
                        
                        
                    </ul>
                </ul>
            </div>
        </div>
    
        
        
        
        
        
        
        
        
        
        
        
        

        
        
        
        
        
        
        
        
        
        
        
        
        



        
        
        
        

        <div class="registerBox registerBoxBank margBtm20">
            
            
                
                    <div class="boxIcons">
                    
                        

                            <a href="/epz/order/notice/printForm/list.html?regNumber=0361200015019004764" class="cryptoSignLink linkPopUp pWidth_840">
                            </a>
                        
                        
                    
                        
                            
                                <a href="/epz/order/notice/printForm/view.html?regNumber=0361200015019004764" target="_blank" class="printLink"></a>
                            
                            
                        
                    </div>
                
            
            <table cellspacing="0" cellpadding="0">
                <tbody><tr>
                    <td class="tenderTd" style=" width: 26%">
                        <dl>
                            
                            <dt>
                                <strong>
                                    
                                        
                                        
                                            Электронный аукцион
                                        
                                    
                                </strong>
                            </dt>
                            <dd>
                                    
                                
                            </dd>
                            <dt>
                                
                                    
                                        
                                            
                                            
                                            
                                            
                                            <span class="checked noWrap">
                                                                            
                                                                            Процедура завершена /
                                                                            
                                                                        
                                                    
                                                    <span class="orange">44-ФЗ</span></span>
                                            
                                            
                                        
                                    
                                    
                                
                            </dt>
                            
                            <dd>
                                
                                    <span class="greyText">Начальная цена</span><br>
                                    <strong>
                                        

                                        258&nbsp;145
                                        <span class="fractionNumber">,82</span>
                                    </strong><br><span class="currency">Российский рубль</span>
                                
                            </dd>
                            <dd>
                                
                            </dd>
                        </dl>
                    </td>

                    <td class="descriptTenderTd">
                        <dl>
                            <dt>
                                <a target="_blank" href="/epz/order/notice/ea44/view/common-info.html?regNumber=0361200015019004764">
                                    № 0361200015019004764
                                </a>
                                    
                                    
                                
                            </dt>
                            <dd class="nameOrganization">
                                
                                    
                                    
                                    
                                        
                                            
                                                Организация, осуществляющая размещение:
                                                <ul>
                                                    <li>
                                                        <a target="_blank" href="/epz/organization/view/info.html?organizationId=1393813" onclick="window.open(this.href); return false;">
                                                            ГОСУДАРСТВЕННОЕ КАЗЕННОЕ УЧРЕЖДЕНИЕ "ЦЕНТР ГОСУДАРСТВЕННЫХ ЗАКУПОК САХАЛИНСКОЙ ОБЛАСТИ"
                                                        </a>
                                                    </li>
                                                </ul>
                                            
                                            
                                        
                                    
                                
                            </dd>
                            <dd>
                                Поставка реагентов для автоматического биохимического анализатора Vitalit-1000 (2)
                                <ul></ul>
                            </dd>
                            
                                <dd class="padTop10">
                                    Идентификационный код закупки(ИКЗ):
                                    <dl class="greyText margTop0 padTop8">
                                        









    192651000352165100100102220010000000



                                    </dl>
                                </dd>
                            
                            
                            
                        </dl>
                    </td>

                    <td class="amountTenderTd">
                        <ul>
                            <li><label>Размещено:</label> 22.07.2019</li>
                            <li><label>Обновлено:</label> 05.08.2019</li>
                        </ul>
                    </td>
                </tr>
                
            </tbody></table>
            <div class="reportBox">
                <ul>
                    <ul>
                            
                        <li><a href="/epz/order/notice/ea44/view/common-info.html?regNumber=0361200015019004764" target="_blank">
                            Сведения</a>
                        </li>

                            
                        <li>
                            <a href="/epz/order/notice/ea44/view/documents.html?regNumber=0361200015019004764" target="_blank">
                            Документы</a>
                        </li>

                            
                        

                        
                            
                            <li><a onclick="openComplaintQuickSearch('0361200015019004764', false, false, true)" style="cursor: pointer;">
                                Жалобы</a>
                            </li>
                        


                        
                            
                            
                            
                            
                        

                            
                            
                            
                        

                            
                            
                        
                            <li><a onclick="openContractUrl('0361200015019004764')" style="cursor: pointer;">
                                Контракты</a>
                            </li>
                        

                            
                        
                        
                            <li><a onclick="bankGuaranteeUrl('0361200015019004764')" style="cursor: pointer;">
                                Банковские гарантии</a>
                            </li>
                        
                        
                    </ul>
                </ul>
            </div>
        </div>
    
        
        
        
        
        
        
        
        
        
        
        
        

        
        
        
        
        
        
        
        
        
        
        
        
        



        
        
        
        

        <div class="registerBox registerBoxBank margBtm20">
            
            
                
                    <div class="boxIcons">
                    
                        

                            <a href="/epz/order/notice/printForm/list.html?regNumber=0161300006319000202" class="cryptoSignLink linkPopUp pWidth_840">
                            </a>
                        
                        
                    
                        
                            
                                <a href="/epz/order/notice/printForm/view.html?regNumber=0161300006319000202" target="_blank" class="printLink"></a>
                            
                            
                        
                    </div>
                
            
            <table cellspacing="0" cellpadding="0">
                <tbody><tr>
                    <td class="tenderTd" style=" width: 26%">
                        <dl>
                            
                            <dt title="Электронный аукцион на проведение работ по строительству, реконструкции, кап. ремонту, сносу объекта кап. строительства, предусматривающих проектную документацию, утвержденную в порядке, установленном законодательством о градостроительной деятельности">
                                <strong>
                                    
                                        
                                            Электронный аукцион на проведение работ по строительству, реконструкции, кап. ремонту, сносу объекта кап. строительства, предусматривающих проектную документацию, утвержденную в по...
                                        
                                        
                                    
                                </strong>
                            </dt>
                            <dd>
                                    
                                
                            </dd>
                            <dt>
                                
                                    
                                        
                                            
                                                <span class="fzNews noWrap">Подача заявок /
                                                    
                                                    <span class="orange">44-ФЗ</span></span>
                                            
                                            
                                            
                                            
                                            
                                        
                                    
                                    
                                
                            </dt>
                            
                            <dd>
                                
                                    <span class="greyText">Начальная цена</span><br>
                                    <strong>
                                        

                                        106&nbsp;376&nbsp;180
                                        <span class="fractionNumber">,00</span>
                                    </strong><br><span class="currency">Российский рубль</span>
                                
                            </dd>
                            <dd>
                                
                            </dd>
                        </dl>
                    </td>

                    <td class="descriptTenderTd">
                        <dl>
                            <dt>
                                <a target="_blank" href="/epz/order/notice/ea44/view/common-info.html?regNumber=0161300006319000202">
                                    № 0161300006319000202
                                </a>
                                    
                                    
                                
                            </dt>
                            <dd class="nameOrganization">
                                
                                    
                                    
                                    
                                        
                                            
                                            
                                                Заказчик:
                                                <ul>
                                                    <li>
                                                        
                                                            
                                                                
                                                                    <a target="_blank" href="/epz/organization/view/info.html?organizationId=733270" onclick="window.open(this.href); return false;">
                                                                        АДМИНИСТРАЦИЯ МУНИЦИПАЛЬНОГО ОБРАЗОВАНИЯ ГОРОДСКОЙ ОКРУГ "ДОЛИНСКИЙ" САХАЛИНСКОЙ ОБЛАСТИ РОССИЙСКОЙ ФЕДЕРАЦИИ
                                                                    </a>
                                                                
                                                            
                                                            
                                                        
                                                    </li>
                                                </ul>
                                            
                                        
                                    
                                
                            </dd>
                            <dd>
                                Строительство многоквартирного дома в с. Покровка
                                <ul></ul>
                            </dd>
                            
                                <dd class="padTop10">
                                    Идентификационный код закупки(ИКЗ):
                                    <dl class="greyText margTop0 padTop8">
                                        









    193650300045665030100100290014120414



                                    </dl>
                                </dd>
                            
                            
                            
                        </dl>
                    </td>

                    <td class="amountTenderTd">
                        <ul>
                            <li><label>Размещено:</label> 05.08.2019</li>
                            <li><label>Обновлено:</label> 05.08.2019</li>
                        </ul>
                    </td>
                </tr>
                
            </tbody></table>
            <div class="reportBox">
                <ul>
                    <ul>
                            
                        <li><a href="/epz/order/notice/ea44/view/common-info.html?regNumber=0161300006319000202" target="_blank">
                            Сведения</a>
                        </li>

                            
                        <li>
                            <a href="/epz/order/notice/ea44/view/documents.html?regNumber=0161300006319000202" target="_blank">
                            Документы</a>
                        </li>

                            
                        

                        
                            
                            <li><a onclick="openComplaintQuickSearch('0161300006319000202', false, false, true)" style="cursor: pointer;">
                                Жалобы</a>
                            </li>
                        


                        
                            
                            
                            
                            
                        

                            
                            
                            
                        

                            
                            
                        

                            
                        
                        
                            <li><a onclick="bankGuaranteeUrl('0161300006319000202')" style="cursor: pointer;">
                                Банковские гарантии</a>
                            </li>
                        
                        
                    </ul>
                </ul>
            </div>
        </div>
    
    <div class="margBtm50">
        














    



    <div class="paginator greyBox "> 
        
            
                
                
                    
                    




<p class="allRecords">





    Всего записей: более <strong>25&nbsp;000&nbsp;000</strong><!-- total: 25 176 984-->
    
</p>
                
            
            
                
                    






















    




    
        
        
    
    



    



    
    
        
    


<ul class="pages">
    

    

    
    

    
    

        

        

        

        

        

        
    


    <li class="page">
        <a class="page__link page__link_active">
            <span class="link-text">1</span>
        </a>
    </li>


    
    

        

        
            
                
                    <li class="page">
                        <a href="javascript:goToPage(2)" data-pagenumber="2" class="page__link">
                            <span class="link-text">2</span>
                        </a>
                    </li>
                
                
            
        

        

        
            
                
                    <li class="page">
                        <a href="javascript:goToPage(3)" data-pagenumber="3" class="page__link">
                            <span class="link-text">3</span>
                        </a>
                    </li>
                
                
            
        

        
        
            <li class="page">
                <span class="link-text-enum">...</span>
            </li>
        
        

        

        
            
                
                    <li class="page">
                        <a href="javascript:goToPage(100)" data-pagenumber="100" class="page__link">
                            <span class="link-text">100</span>
                        </a>
                    </li>
                
                
            
        
    

    
    

    

    
        
            
                <a href="javascript:goToPage(2)" data-pagenumber="2" class="paginator-button paginator-button-next"><img src="/epz/order/quicksearch/img/icons/arrow-prime.svg" alt=""></a>
            
            
        
    
</ul>

                    
                
                
            
        
        

    </div>




        <div class="clear"></div>
    </div>
    
</div>

<script type="text/javascript">

    function serializeForDiffCheck(formSelector) {
        return $(formSelector).serialize().replace(/\+/g, '').replace(/pageNo=\d/, '');
    }
</script>


    
    
    








































<footer class="footer">
    <div class="wrapperFooter">
        
            
            
                
                    <div class="container">
                        <div class="poll-banner">
                            <div class="row align-items-center">
                                <div class="col-9">
                                    <div class="figure-footer d-flex align-items-center">
                                        <div class="figure-footer__icon">
                                            <img src="/epz/order/quicksearch/img/icons/ico_sub.svg" alt="" class="icon">
                                        </div>
                                        <div class="figure-footer__text">
                                            <h4 class="heading-h4 poll-title">Поделитесь мнением о качестве работы единой
                                                информационной системы</h4>
                                        </div>
                                    </div>
                                </div>
                                <div class="col-3 text-right">
                                    <a href="/epz/main/public/quiz/list.html" class="btn btn-default poll-button">
                                        <span class="separator"></span>
                                        <span class="btn-text">Перейти к опросу</span>
                                    </a>
                                </div>
                            </div>
                            <figure class="poll__logo">
                                <img src="/epz/order/quicksearch/img/icons/icon-footer-eagle.svg" alt="">
                            </figure>
                        </div>
                    </div>
                
                <div class="container">
                    <div class="partners-wrap">
                        <div class="partners partners-slider slick-initialized slick-slider"><div class="slick-list draggable"><div class="slick-track" style="opacity: 1; width: 3840px; transform: translate3d(-2080px, 0px, 0px); transition: transform 500ms ease 0s;"><div class="slick-slide slick-cloned" data-slick-index="-6" aria-hidden="true" style="width: 160px;" tabindex="-1"><div><figure class="partner" style="width: 100%; display: inline-block;">
                                <p class="partner-logo-wrap">
                                    <a target="_blank" href="http://www.rts-tender.ru/" tabindex="-1"><img class="partner__logo" src="/epz/order/quicksearch/img/partners/rts.svg" alt=""></a>
                                </p>
                                <figcaption class="partner__desc"> Электронная площадка <br> России
                                </figcaption>
                                <a target="_blank" href="http://www.rts-tender.ru/" class="partner__link" tabindex="-1">rts-tender.ru</a>
                            </figure></div></div><div class="slick-slide slick-cloned" data-slick-index="-5" aria-hidden="true" style="width: 160px;" tabindex="-1"><div><figure class="partner" style="width: 100%; display: inline-block;">
                                <p class="partner-logo-wrap">
                                    <a target="_blank" href="http://etp-ets.ru/" tabindex="-1"><img class="partner__logo" src="/epz/order/quicksearch/img/partners/ets.svg" alt=""></a>
                                </p>
                                <figcaption class="partner__desc"> Национальная электронная <br> площадка
                                </figcaption>
                                <a target="_blank" href="http://etp-ets.ru/" class="partner__link" tabindex="-1">etp-ets.ru</a>
                            </figure></div></div><div class="slick-slide slick-cloned" data-slick-index="-4" aria-hidden="true" style="width: 160px;" tabindex="-1"><div><figure class="partner" style="width: 100%; display: inline-block;">
                                <p class="partner-logo-wrap">
                                    <a target="_blank" href="https://gz.lot-online.ru" tabindex="-1"><img class="partner__logo" src="/epz/order/quicksearch/img/partners/newGZ.svg" alt=""></a>
                                </p>
                                <figcaption class="partner__desc"> Всероссийская <br> универсальная площадка
                                </figcaption>
                                <a target="_blank" href="https://gz.lot-online.ru" class="partner__link" tabindex="-1">gz.lot-online.ru</a>
                            </figure></div></div><div class="slick-slide slick-cloned" data-slick-index="-3" aria-hidden="true" style="width: 160px;" tabindex="-1"><div><figure class="partner" style="width: 100%; display: inline-block;">
                                <p class="partner-logo-wrap">
                                    <a target="_blank" href="https://www.tektorg.ru/" tabindex="-1"><img class="partner__logo" src="/epz/order/quicksearch/img/partners/tektorg_new.svg" alt=""></a>
                                </p>
                                <figcaption class="partner__desc"> Федеральная электронная<br>площадка ТЭК-Торг

                                </figcaption>
                                <a target="_blank" href="https://www.tektorg.ru/" class="partner__link" tabindex="-1">tektorg.ru</a>
                            </figure></div></div><div class="slick-slide slick-cloned" data-slick-index="-2" aria-hidden="true" style="width: 160px;" tabindex="-1"><div><figure class="partner" style="width: 100%; display: inline-block;">
                                <p class="partner-logo-wrap">
                                    <a target="_blank" href="https://etpgpb.ru/" tabindex="-1"><img class="partner__logo" src="/epz/order/quicksearch/img/partners/etpgpb.svg" alt=""></a>
                                </p>
                                <figcaption class="partner__desc"> Электронная торговая<br>площадка ГПБ
                                </figcaption>
                                <a target="_blank" href="https://etpgpb.ru/" class="partner__link" tabindex="-1">etpgpb.ru</a>
                            </figure></div></div><div class="slick-slide slick-cloned" data-slick-index="-1" aria-hidden="true" style="width: 160px;" tabindex="-1"><div><figure class="partner" style="width: 100%; display: inline-block;">
                                <p class="partner-logo-wrap">
                                    <a target="_blank" href="http://www.astgoz.ru/" tabindex="-1"><img class="partner__logo" src="/epz/order/quicksearch/img/partners/astgoz.svg" alt=""></a>
                                </p>
                                <figcaption class="partner__desc"> Автоматизированная система торгов государственного
                                    оборонного
                                    заказа <br></figcaption>
                                <a target="_blank" href="http://www.astgoz.ru/" class="partner__link" tabindex="-1">astgoz.ru</a>
                            </figure></div></div><div class="slick-slide" data-slick-index="0" aria-hidden="true" style="width: 160px;" tabindex="-1"><div><figure class="partner" style="width: 100%; display: inline-block;">
                                <p class="partner-logo-wrap">
                                    <a target="_blank" href="http://www.sberbank-ast.ru/" tabindex="-1"><img class="partner__logo" src="/epz/order/quicksearch/img/partners/sberbank.svg" alt=""></a>
                                </p>
                                <figcaption class="partner__desc"> Система торгов <br> Сбербанк-АСТ
                                </figcaption>
                                <a target="_blank" href="http://www.sberbank-ast.ru/" class="partner__link" tabindex="-1">sberbank-ast.ru</a>
                            </figure></div></div><div class="slick-slide" data-slick-index="1" aria-hidden="true" style="width: 160px;" tabindex="-1"><div><figure class="partner" style="width: 100%; display: inline-block;">
                                <p class="partner-logo-wrap">
                                    <a target="_blank" href="http://www.roseltorg.ru/" tabindex="-1"><img class="partner__logo" src="/epz/order/quicksearch/img/partners/rostorg.svg" alt=""></a>
                                </p>
                                <figcaption class="partner__desc"> Единая электронная торговая <br> площадка
                                </figcaption>
                                <a target="_blank" href="http://www.roseltorg.ru/" class="partner__link" tabindex="-1">roseltorg.ru</a>
                            </figure></div></div><div class="slick-slide" data-slick-index="2" aria-hidden="true" style="width: 160px;" tabindex="-1"><div><figure class="partner" style="width: 100%; display: inline-block;">
                                <p class="partner-logo-wrap">
                                    <a target="_blank" href="http://etp.zakazrf.ru/" tabindex="-1"><img class="partner__logo" src="/epz/order/quicksearch/img/partners/etp.svg" alt=""></a>
                                </p>
                                <figcaption class="partner__desc"> Общероссийская система <br> электронной торговли
                                </figcaption>
                                <a target="_blank" href="http://etp.zakazrf.ru/" class="partner__link" tabindex="-1">etp.zakazrf.ru</a>
                            </figure></div></div><div class="slick-slide" data-slick-index="3" aria-hidden="true" style="width: 160px;" tabindex="-1"><div><figure class="partner" style="width: 100%; display: inline-block;">
                                <p class="partner-logo-wrap">
                                    <a target="_blank" href="http://www.rts-tender.ru/" tabindex="-1"><img class="partner__logo" src="/epz/order/quicksearch/img/partners/rts.svg" alt=""></a>
                                </p>
                                <figcaption class="partner__desc"> Электронная площадка <br> России
                                </figcaption>
                                <a target="_blank" href="http://www.rts-tender.ru/" class="partner__link" tabindex="-1">rts-tender.ru</a>
                            </figure></div></div><div class="slick-slide" data-slick-index="4" aria-hidden="true" style="width: 160px;" tabindex="-1"><div><figure class="partner" style="width: 100%; display: inline-block;">
                                <p class="partner-logo-wrap">
                                    <a target="_blank" href="http://etp-ets.ru/" tabindex="-1"><img class="partner__logo" src="/epz/order/quicksearch/img/partners/ets.svg" alt=""></a>
                                </p>
                                <figcaption class="partner__desc"> Национальная электронная <br> площадка
                                </figcaption>
                                <a target="_blank" href="http://etp-ets.ru/" class="partner__link" tabindex="-1">etp-ets.ru</a>
                            </figure></div></div><div class="slick-slide" data-slick-index="5" aria-hidden="true" style="width: 160px;" tabindex="-1"><div><figure class="partner" style="width: 100%; display: inline-block;">
                                <p class="partner-logo-wrap">
                                    <a target="_blank" href="https://gz.lot-online.ru" tabindex="-1"><img class="partner__logo" src="/epz/order/quicksearch/img/partners/newGZ.svg" alt=""></a>
                                </p>
                                <figcaption class="partner__desc"> Всероссийская <br> универсальная площадка
                                </figcaption>
                                <a target="_blank" href="https://gz.lot-online.ru" class="partner__link" tabindex="-1">gz.lot-online.ru</a>
                            </figure></div></div><div class="slick-slide" data-slick-index="6" aria-hidden="true" style="width: 160px;"><div><figure class="partner" style="width: 100%; display: inline-block;">
                                <p class="partner-logo-wrap">
                                    <a target="_blank" href="https://www.tektorg.ru/" tabindex="0"><img class="partner__logo" src="/epz/order/quicksearch/img/partners/tektorg_new.svg" alt=""></a>
                                </p>
                                <figcaption class="partner__desc"> Федеральная электронная<br>площадка ТЭК-Торг

                                </figcaption>
                                <a target="_blank" href="https://www.tektorg.ru/" class="partner__link" tabindex="0">tektorg.ru</a>
                            </figure></div></div><div class="slick-slide slick-current slick-active" data-slick-index="7" aria-hidden="false" style="width: 160px;"><div><figure class="partner" style="width: 100%; display: inline-block;">
                                <p class="partner-logo-wrap">
                                    <a target="_blank" href="https://etpgpb.ru/" tabindex="0"><img class="partner__logo" src="/epz/order/quicksearch/img/partners/etpgpb.svg" alt=""></a>
                                </p>
                                <figcaption class="partner__desc"> Электронная торговая<br>площадка ГПБ
                                </figcaption>
                                <a target="_blank" href="https://etpgpb.ru/" class="partner__link" tabindex="0">etpgpb.ru</a>
                            </figure></div></div><div class="slick-slide slick-active" data-slick-index="8" aria-hidden="false" style="width: 160px;"><div><figure class="partner" style="width: 100%; display: inline-block;">
                                <p class="partner-logo-wrap">
                                    <a target="_blank" href="http://www.astgoz.ru/" tabindex="0"><img class="partner__logo" src="/epz/order/quicksearch/img/partners/astgoz.svg" alt=""></a>
                                </p>
                                <figcaption class="partner__desc"> Автоматизированная система торгов государственного
                                    оборонного
                                    заказа <br></figcaption>
                                <a target="_blank" href="http://www.astgoz.ru/" class="partner__link" tabindex="0">astgoz.ru</a>
                            </figure></div></div><div class="slick-slide slick-cloned slick-active" data-slick-index="9" aria-hidden="false" style="width: 160px;" tabindex="-1"><div><figure class="partner" style="width: 100%; display: inline-block;">
                                <p class="partner-logo-wrap">
                                    <a target="_blank" href="http://www.sberbank-ast.ru/" tabindex="0"><img class="partner__logo" src="/epz/order/quicksearch/img/partners/sberbank.svg" alt=""></a>
                                </p>
                                <figcaption class="partner__desc"> Система торгов <br> Сбербанк-АСТ
                                </figcaption>
                                <a target="_blank" href="http://www.sberbank-ast.ru/" class="partner__link" tabindex="0">sberbank-ast.ru</a>
                            </figure></div></div><div class="slick-slide slick-cloned slick-active" data-slick-index="10" aria-hidden="false" style="width: 160px;" tabindex="-1"><div><figure class="partner" style="width: 100%; display: inline-block;">
                                <p class="partner-logo-wrap">
                                    <a target="_blank" href="http://www.roseltorg.ru/" tabindex="0"><img class="partner__logo" src="/epz/order/quicksearch/img/partners/rostorg.svg" alt=""></a>
                                </p>
                                <figcaption class="partner__desc"> Единая электронная торговая <br> площадка
                                </figcaption>
                                <a target="_blank" href="http://www.roseltorg.ru/" class="partner__link" tabindex="0">roseltorg.ru</a>
                            </figure></div></div><div class="slick-slide slick-cloned slick-active" data-slick-index="11" aria-hidden="false" style="width: 160px;" tabindex="-1"><div><figure class="partner" style="width: 100%; display: inline-block;">
                                <p class="partner-logo-wrap">
                                    <a target="_blank" href="http://etp.zakazrf.ru/" tabindex="0"><img class="partner__logo" src="/epz/order/quicksearch/img/partners/etp.svg" alt=""></a>
                                </p>
                                <figcaption class="partner__desc"> Общероссийская система <br> электронной торговли
                                </figcaption>
                                <a target="_blank" href="http://etp.zakazrf.ru/" class="partner__link" tabindex="0">etp.zakazrf.ru</a>
                            </figure></div></div><div class="slick-slide slick-cloned slick-active" data-slick-index="12" aria-hidden="false" style="width: 160px;" tabindex="-1"><div><figure class="partner" style="width: 100%; display: inline-block;">
                                <p class="partner-logo-wrap">
                                    <a target="_blank" href="http://www.rts-tender.ru/" tabindex="-1"><img class="partner__logo" src="/epz/order/quicksearch/img/partners/rts.svg" alt=""></a>
                                </p>
                                <figcaption class="partner__desc"> Электронная площадка <br> России
                                </figcaption>
                                <a target="_blank" href="http://www.rts-tender.ru/" class="partner__link" tabindex="-1">rts-tender.ru</a>
                            </figure></div></div><div class="slick-slide slick-cloned" data-slick-index="13" aria-hidden="true" style="width: 160px;" tabindex="-1"><div><figure class="partner" style="width: 100%; display: inline-block;">
                                <p class="partner-logo-wrap">
                                    <a target="_blank" href="http://etp-ets.ru/" tabindex="-1"><img class="partner__logo" src="/epz/order/quicksearch/img/partners/ets.svg" alt=""></a>
                                </p>
                                <figcaption class="partner__desc"> Национальная электронная <br> площадка
                                </figcaption>
                                <a target="_blank" href="http://etp-ets.ru/" class="partner__link" tabindex="-1">etp-ets.ru</a>
                            </figure></div></div><div class="slick-slide slick-cloned" data-slick-index="14" aria-hidden="true" style="width: 160px;" tabindex="-1"><div><figure class="partner" style="width: 100%; display: inline-block;">
                                <p class="partner-logo-wrap">
                                    <a target="_blank" href="https://gz.lot-online.ru" tabindex="-1"><img class="partner__logo" src="/epz/order/quicksearch/img/partners/newGZ.svg" alt=""></a>
                                </p>
                                <figcaption class="partner__desc"> Всероссийская <br> универсальная площадка
                                </figcaption>
                                <a target="_blank" href="https://gz.lot-online.ru" class="partner__link" tabindex="-1">gz.lot-online.ru</a>
                            </figure></div></div><div class="slick-slide slick-cloned" data-slick-index="15" aria-hidden="true" style="width: 160px;" tabindex="-1"><div><figure class="partner" style="width: 100%; display: inline-block;">
                                <p class="partner-logo-wrap">
                                    <a target="_blank" href="https://www.tektorg.ru/" tabindex="-1"><img class="partner__logo" src="/epz/order/quicksearch/img/partners/tektorg_new.svg" alt=""></a>
                                </p>
                                <figcaption class="partner__desc"> Федеральная электронная<br>площадка ТЭК-Торг

                                </figcaption>
                                <a target="_blank" href="https://www.tektorg.ru/" class="partner__link" tabindex="-1">tektorg.ru</a>
                            </figure></div></div><div class="slick-slide slick-cloned" data-slick-index="16" aria-hidden="true" style="width: 160px;" tabindex="-1"><div><figure class="partner" style="width: 100%; display: inline-block;">
                                <p class="partner-logo-wrap">
                                    <a target="_blank" href="https://etpgpb.ru/" tabindex="-1"><img class="partner__logo" src="/epz/order/quicksearch/img/partners/etpgpb.svg" alt=""></a>
                                </p>
                                <figcaption class="partner__desc"> Электронная торговая<br>площадка ГПБ
                                </figcaption>
                                <a target="_blank" href="https://etpgpb.ru/" class="partner__link" tabindex="-1">etpgpb.ru</a>
                            </figure></div></div><div class="slick-slide slick-cloned" data-slick-index="17" aria-hidden="true" style="width: 160px;" tabindex="-1"><div><figure class="partner" style="width: 100%; display: inline-block;">
                                <p class="partner-logo-wrap">
                                    <a target="_blank" href="http://www.astgoz.ru/" tabindex="-1"><img class="partner__logo" src="/epz/order/quicksearch/img/partners/astgoz.svg" alt=""></a>
                                </p>
                                <figcaption class="partner__desc"> Автоматизированная система торгов государственного
                                    оборонного
                                    заказа <br></figcaption>
                                <a target="_blank" href="http://www.astgoz.ru/" class="partner__link" tabindex="-1">astgoz.ru</a>
                            </figure></div></div></div></div></div>
                        <span class="partners-slider__btn partners-slider__btn_prev slick-arrow" style="">
                    <img src="/epz/order/quicksearch/img/icons/arrow_blue.svg" alt="">
                </span> 
                        <span class="partners-slider__btn partners-slider__btn_next slick-arrow" style="">
                    <img src="/epz/order/quicksearch/img/icons/arrow_blue.svg" alt="">
                </span> 
                    </div>
                </div>
                <section class="footer-nav">
                    <div class="container">
                        <div class="row">
                            <div class="col-md-12 col-lg-12">
                                <ul class="footer-nav-list">
                                    <li class="footer-nav__item">
                                        <a href="/epz/main/public/news/news-search.html" class="footer-nav__link">Новости</a>
                                    </li>
                                    <li class="footer-nav__item">
                                        <a href="/epz/main/public/forSuppliers.html" class="footer-nav__link">Поставщикам</a>
                                    </li>
                                    <li class="footer-nav__item">
                                        <a href="/epz/main/public/forCustomers.html" class="footer-nav__link">Заказчикам</a>
                                    </li>
                                    <li class="footer-nav__item">
                                        <a href="/epz/main/public/quiz/list.html" class="footer-nav__link">Опросы</a>
                                    </li>
                                    <li class="footer-nav__item">
                                        <a href="/epz/main/public/home.html#statAnchor" class="footer-nav__link">Статистика</a>
                                    </li>
                                    <li class="footer-nav__item">
                                        <a target="_blank" href="http://zakupki.gov.ru/forum/forums/list.page" class="footer-nav__link">Форум</a>
                                    </li>
                                    <li class="footer-nav__item">
                                        <a data-modalup="" href="/epz/main/public/siteMap.html" class="footer-nav__link">Карта сайта</a>
                                    </li>
                                    <li class="footer-nav__item">
                                        <a href="http://zakupki.gov.ru/rpt/cat02/zakupki-traffic.xlsx" class="footer-nav__link">Отчет о посещаемости</a>
                                    </li>
                                    <li class="footer-nav__item">
                                        <a href="/epz/main/public/qa/view.html" class="footer-nav__link">Часто задаваемые вопросы</a>
                                    </li>
                                </ul>
                            </div>
                        </div>
                    </div>
                </section>
                <section class="footer-links">
                    <div class="container">
                        <div class="row">
                            <div class="col-4 col-sm-4 col-md-4 col-lg-4">
                                <figure class="logo">
                                    <img src="/epz/order/quicksearch/img/header/emblem.svg" alt="" class="logo__img">
                                    <figcaption class="logo__name"> Единая информационная система<br> в сфере закупок</figcaption>
                                </figure>
                                <div class="copyright">
                                    <small class="copyright__text">© Федеральное казначейство, 2019</small>
                                    <small class="copyright__text"> Версия 9.2.3.3 rev 2502a52d96 от 02.08.2019</small>
                                </div>
                            </div>
                            <div class="col-4 col-sm-4 col-md-4 col-lg-4">
                                <nav class="usefull-links">
                                    <span class="list-title">Официальные ресурсы</span>
                                    <ul class="list">
                                        <li class="list-item">
                                            <a target="_blank" href="http://www.kremlin.ru" class="list-item__link">Президент Российской Федерации</a>
                                        </li>
                                        <li class="list-item">
                                            <a target="_blank" href="http://www.government.ru" class="list-item__link">Правительство Российской Федерации</a>
                                        </li>
                                        <li class="list-item">
                                            <a target="_blank" href="http://www.minfin.ru" class="list-item__link">Министерство финансов Российской Федерации</a>
                                        </li>
                                        <li class="list-item">
                                            <a target="_blank" href="http://www.fas.gov.ru" class="list-item__link">Федеральная антимонопольная служба</a>
                                        </li>
                                        <li class="list-item">
                                            <a target="_blank" href="http://www.economy.gov.ru" class="list-item__link">Министерство экономического развития Российской Федерации</a>
                                        </li>
                                        <li class="list-item">
                                            <a target="_blank" href="http://roskazna.ru" class="list-item__link">Федеральное казначейство</a>
                                        </li>
                                    </ul>
                                </nav>
                            </div>
                            <div class="col-4 col-sm-4 col-md-4 col-lg-4">
                                <nav class="usefull-links">
                                    <span class="list-title">Техническая информация</span>
                                    <ul class="list">
                                        <li class="list-item">
                                            <a href="/epz/main/public/user-feedback.html" class="list-item__link">Техническая поддержка</a>
                                        </li>
                                        <li class="list-item">
                                            <a data-modalup="" href="/epz/main/public/userFeedback/openFeedbackForm.html" class="list-item__link">Ваши идеи по улучшению сайта</a>
                                        </li>
                                    </ul>
                                </nav>
                                <figure class="btn-on-top">
                                    <a class="btn-on-top__link">
                                        <img class="btn-on-top__image" src="/epz/order/quicksearch/img/icons/arrow-on-top.svg" alt="">
                                    </a>
                                </figure>
                            </div>
                        </div>
                    </div>
                </section>
            
        
        <div class="clear"></div>
    </div>
</footer>
<script src="/epz/order/quicksearch/js/ymaps/ymaps.js" type="text/javascript"></script>


<script type="text/javascript">
    var isRegisteredUserObozApp = Boolean("");
    var sessionMaxInactiveInterval = "180";
    $(document).ready(function () {

        /* fix console.log in IE */
        if (!window.console) window.console = {};
        if (!window.console.log) window.console.log = function () { };
        /* fix console.log in IE */

        var userRegionName = $.cookie("userRegionName"),
                userRegionId = $.cookie("userRegionId"),
                doNotShowKladrPopUp = $.cookie("doNotShowKladrPopUp"),
                doNotUseRegionToFind = $.cookie("doNotUseRegionToFind"),
                doNotAdviseToChangeLocation = $.cookie("doNotAdviseToChangeLocation"),
                goodVisionLink = $(document).find('.goodVisionLink');

        function detectGeolocation(callback) {
            ymaps.ready(function () {
                ymaps.geolocation.get({
                    provider: 'yandex',
                    autoReverseGeocode: true
                }).then(function (result) {
                    callback(result);
                });
            });
        }

        function getRegionIdByName(regionName, callback) {
            $.get('/epz/nsi/kladr/regionIdByName.json', {regionName : regionName}).done(function(data) {
                callback(data);
            });
        }

        function getAdministrativeAreaName(responseFromYandexGeolocationService) {
            return responseFromYandexGeolocationService.geoObjects.get(0).properties.get('metaDataProperty.GeocoderMetaData.AddressDetails.Country.AdministrativeArea.AdministrativeAreaName');
        }

        function getSubAdministrativeAreaName(responseFromYandexGeolocationService) {
            return responseFromYandexGeolocationService.geoObjects.get(0).properties.get('metaDataProperty.GeocoderMetaData.AddressDetails.Country.AdministrativeArea.SubAdministrativeArea.SubAdministrativeAreaName');
        }

        goodVisionLink.click(function (e) {
            e.preventDefault();
            $.removeCookie('usePoorVisionOption', { path: '/'});
            $.removeCookie('colorSpectrumForPoorVision', { path: '/'});
            $.removeCookie('fontSizeForPoorVision', { path: '/'});
            location.reload();
        });

        if (userRegionId != null && userRegionId != 0) {
            setRegionNameHeader(userRegionName);
            if(doNotUseRegionToFind != 'true' && doNotAdviseToChangeLocation != 'true') {
                detectGeolocation(function(responseFromYandexGeolocationService) {
                    var administrativeAreaName = getAdministrativeAreaName(responseFromYandexGeolocationService),
                            subAdministrativeAreaName = getSubAdministrativeAreaName(responseFromYandexGeolocationService),
                            preparedUserRegionName = null;

                    if (findFederalRegionYandexAnswer(administrativeAreaName)) {
                        userRegionName = subAdministrativeAreaName;
                    } else {
                        userRegionName = administrativeAreaName;
                    }

                    preparedUserRegionName = prepareYandexRegionName(userRegionName);

                    if(preparedUserRegionName && preparedUserRegionName.trim()) {
                        getRegionIdByName(preparedUserRegionName, function(data) {
                            var regionId = data ? data.regionId : null;
                            if(regionId && regionId != userRegionId) {
                                $.cookie("possibleRegionIdChange", regionId, { path: '/epz', expires: 1 });
                                $("#chooseRegion").click();
                            }
                        });
                    }

                });
            }
        } else {
            setRegionNameHeader("Не выбран");

            detectGeolocation(function(responseFromYandexGeolocationService) {
                var administrativeAreaName = getAdministrativeAreaName(responseFromYandexGeolocationService),
                        subAdministrativeAreaName = getSubAdministrativeAreaName(responseFromYandexGeolocationService);

                if (findFederalRegionYandexAnswer(administrativeAreaName)) {
                    userRegionName = subAdministrativeAreaName;
                } else {
                    userRegionName = administrativeAreaName;
                }

                $.cookie("userRegionName", prepareYandexRegionName(userRegionName), { path: '/epz', expires: 182 });
                $.cookie("yandexRegionName", administrativeAreaName + ', ' + subAdministrativeAreaName, { path: '/epz', expires: 182 });

                if (doNotShowKladrPopUp != 'true') {
                    $("#chooseRegion").click();
                }
            });
        }

        $(".poorVisionLink").click(function(e) {
            e.preventDefault();
            $.cookie('usePoorVisionOption', 'true', {path: '/', expires: 365*100});
            location.reload();
        });
    });

    function setRegionNameHeader(regionName) {
        $("#headerUserRegionName").text(regionName);
    }

    function prepareYandexRegionName(regionName) {
        if (regionName === 'Москва и Московская область') {
            return 'Московская';
        }

        if (regionName === 'Москва и область') {
            return 'Московская';
        }

        if (regionName === 'Санкт-Петербург и Ленинградская область') {
            return 'Ленинградская';
        }

        if (regionName === 'Санкт-Петербург и область') {
            return 'Ленинградская';
        }

        var resultRegionName = null;
        var stringToRemoveArray = [' автономный округ', ' автономная область', ' АО', ' область', ' край', 'Республика ', ' Республика', ' республика'];

        for (var j = 0; j < stringToRemoveArray.length; j++) {
            if (regionName.search(stringToRemoveArray[j]) > -1) {
                resultRegionName = regionName.replace(stringToRemoveArray[j], '');

                break;
            } else {
                resultRegionName = regionName;
            }
        }

        return resultRegionName.split('-')[0];
    }

    function findFederalRegionYandexAnswer(yandexAnswer) {
        var answerArray = yandexAnswer.split(' ');

        for (var i = 0; i < answerArray.length; i++) {
            if (answerArray[i] === 'округ') {
                return true;
            }
        }

        return false;
    }

    /*Отладочная информация - все регионы РФ из ответа Яндекса https://yandex.ru/yaca/geo.c2n */
    /*var yandexRegionNameArray = ['Москва и область', 'Белгородская область', 'Брянская область', 'Владимирcкая область', 'Воронежcкая область', 'Ивановская область', 'Калужская область', 'Костромская область', 'Курская область',
     'Липецкая область', 'Орловская область', 'Рязанская область', 'Смоленская область', 'Тамбовская область', 'Тверская область', 'Тульская область', 'Ярославская область',
     'Санкт-Петербург и Ленинградская область', 'Архангельская область', 'Вологодская область', 'Калининградская область', 'Мурманская область',
     'Новгородская область', 'Псковская область', 'Республика Коми', 'Республика Карелия', 'Ненецкий АО',
     'Астраханская область', 'Волгоградская область', 'Краснодарский край', 'Республика Адыгея', 'Республика Калмыкия', 'Ростовская область',
     'Кировская область', 'Республика Марий Эл', 'Нижегородская область', 'Оренбургская область', 'Пензенская область', 'Пермский край', 'Республика Башкортостан',
     'Республика Мордовия', 'Татарстан', 'Самарская область', 'Саратовская область', 'Удмуртская республика', 'Ульяновская область', 'Чувашская республика',
     'Курганская область', 'Свердловская область', 'Тюменская область', 'Ханты-Мансийский АО', 'Челябинская область', 'Ямало-Ненецкий АО',
     'Алтайский край', 'Иркутская область', 'Кемеровская область', 'Красноярский край', 'Новосибирская область', 'Омская область',
     'Республика Алтай', 'Республика Бурятия', 'Республика Тыва', 'Республика Хакасия', 'Томская область', 'Забайкальский край',
     'Магаданская область', 'Камчатский край', 'Еврейская автономная область', 'Чукотский автономный округ', 'Хабаровский край', 'Приморский край', 'Амурская область', 'Республика Саха (Якутия)', 'Сахалинская область',
     'Республика Дагестан', 'Республика Ингушетия', 'Республика Кабардино-Балкария', 'Республика Северная Осетия-Алания', 'Ставропольский край', 'Карачаево-Черкесская Республика', 'Чеченская Республика', 'Крым', 'Севастополь'];*/
</script>


<!-- Yandex.Metrika counter -->
<script type="text/javascript">
    (function (d, w, c) {
        (w[c] = w[c] || []).push(function() {
            try {
                w.yaCounter36706425 = new Ya.Metrika({
                    id:36706425,
                    clickmap:true,
                    trackLinks:true,
                    accurateTrackBounce:true
                });
            } catch(e) { }
        });

        var n = d.getElementsByTagName("script")[0],
                s = d.createElement("script"),
                f = function () { n.parentNode.insertBefore(s, n); };
        s.type = "text/javascript";
        s.async = true;
        s.src = "https://mc.yandex.ru/metrika/watch.js";

        if (w.opera == "[object Opera]") {
            d.addEventListener("DOMContentLoaded", f, false);
        } else { f(); }
    })(document, window, "yandex_metrika_callbacks");

    function yandexCounterHit(url) {
        if (typeof(yaCounter36706425) != "undefined") {
            yaCounter36706425.hit(url);
        }
    }

    $(document).ready(function () {
        $("a[target=_blank]:not([initialHref])").click(function (event) {
            yandexCounterHit($(this).attr("href"));
        });

        $(document).ajaxSend(function (event, request, settings) {
            yandexCounterHit(settings.url);
        });
    });

</script>
<noscript><div><img src="https://mc.yandex.ru/watch/36706425" style="position:absolute; left:-9999px;" alt="" /></div></noscript>
<!-- /Yandex.Metrika counter -->



<script type="text/javascript">if (window.epzAnalytics) window.epzAnalytics.track();
$(document).ready(function () {
        checkNotice();
});
</script>



<div id="ui-datepicker-div" class="ui-datepicker ui-widget ui-widget-content ui-helper-clearfix ui-corner-all"></div><ul class="ui-autocomplete ui-front ui-menu ui-widget ui-widget-content ui-corner-all" id="ui-id-1" tabindex="0" style="display: none;"></ul></body></html>'''

'''
soup = BeautifulSoup(docs_html3, 'lxml')
content = soup.findAll('div', class_='registerBox')
for cnt in content:
    resSoup = BeautifulSoup(str(cnt), 'lxml')
    result = resSoup.select('div.reportBox li a')[1].attrs["href"]
    if 'http://' not in result:
        result = 'http://zakupki.gov.ru' + result
    print(result)
'''

''''''
soup3 = BeautifulSoup(docs_html2, 'lxml')
idzakupki = soup3.find(text=re.compile(r' №\S{19}')).strip().split(' ')[1]
print(idzakupki)
elem = soup3.find(text=re.compile(r'Протокол признания участника уклонившимся'))
if elem:
    text = elem.parent.parent.parent.select('td')[1].select('div span')[1].text.strip()
    print(text.split(' '))
    print(text.split(' ')[2].split('МСК')[1].strip(')'))
    tz = int(text.split(' ')[2].split('МСК')[1].strip(')')) + 3
    print(tz)
''''''
