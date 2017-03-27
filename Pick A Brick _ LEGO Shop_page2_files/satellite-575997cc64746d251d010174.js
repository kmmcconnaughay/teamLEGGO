_satellite.pushAsyncScript(function(event, target, $variables){
  setLocale(event.detail.locale);
setExchangeRate(event.detail.currencyConversionRate );
//_satellite.setVar('environment', event.detail.env);
_satellite.setVar('isTrackmanProd', isProduction());
_satellite.setVar('UAID', getCookie('UAID'));
_satellite.setVar('surveyPageCount', 0);
_satellite.setVar('surveyPageCountLimit', 3);
});
