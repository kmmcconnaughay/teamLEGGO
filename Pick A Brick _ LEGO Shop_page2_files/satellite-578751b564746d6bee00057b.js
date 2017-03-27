_satellite.pushAsyncScript(function(event, target, $variables){
  _satellite.notify('viewPage', 1);
var titleArray = event.detail.titleArray;
// remove when LEO-XXXX is done
var lastTitle = titleArray[titleArray.length - 1];
titleArray = titleArray.slice(0, titleArray.length - 1);
lastTitle = lastTitle.replace(/( \| lego shop)/g, '');
titleArray.push(lastTitle);
//
var url = createPreviousUrl(event.detail.previousLocation);

var page_type = ((event.detail.page_type) ? event.detail.page_type.toLowerCase() : null);
_satellite.setVar('pageType', page_type);
_satellite.notify('pageType', page_type);

window.callTrackman(function(shopTracking, basicTracking) {
  basicTracking.setContentCulture(_satellite.getVar('currentLocale'));
  if(url) {
    basicTracking.setReferringUrl(url);
  }
  shopTracking.setShipToCountry(_satellite.getVar('currentCountry'));
  
  basicTracking.setChannel('shop', page_type); 
  basicTracking.setPageName(titleArray);
  basicTracking.trackPage();
});

npsSurveryCounter();
});
