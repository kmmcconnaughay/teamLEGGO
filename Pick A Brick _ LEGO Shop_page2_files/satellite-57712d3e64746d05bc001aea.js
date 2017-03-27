_satellite.pushAsyncScript(function(event, target, $variables){
  window.callTrackman(function(shopTracking, basicTracking){
  var label = event.detail.label.toLowerCase();
  var value = event.detail.value;
  basicTracking.setContentCulture(_satellite.getVar('currentLocale'));
	shopTracking.setShipToCountry(_satellite.getVar('currentCountry'));
  if(value == null) {
    value = '';
  }
  shopTracking.refine(label, value);
});
});
