var setLocale = function(locale)
{
  _satellite.setVar('currentLocale', locale);
  _satellite.setVar('currentCountry',locale.substr(3));
};
var convertToUSD = function(amount)
{
  var locale = _satellite.getVar('currentCountry');
  var usd_currency_conversion = 1;
  var amountInUSD = 0;
  
  if(locale!="US" && !(amount===null) && typeof amount === "number") {
  	//Get echange rate
    usd_currency_conversion = _satellite.getVar('USDConversionRate');
  
    
    //Convert amount to USD
    amountInUSD = (parseFloat(amount) * usd_currency_conversion).toFixed(2);
  }
  else
    	amountInUSD = amount;
	
  return amountInUSD;
}

var setExchangeRate = function(usd_currency_conversion)
{
  var default_usd_currency_conversion = 1;
  if(usd_currency_conversion)
    _satellite.setVar('USDConversionRate', usd_currency_conversion);
  else
    _satellite.setVar('USDConversionRate', default_usd_currency_conversion);
}

function checkForNull(value)
{
    return (value === null) ? "" : value
}

var getOrder = function(cartContent) {
  var order = {
    'state': cartContent.shipping.address.state,
    'zip': cartContent.shipping.address.postal_code,
    'purchaseId': cartContent.order_id,
    'paymentMethod': cartContent.payments[0].method,
    'shipToCountry':  _satellite.getVar('currentCountry'),
    'shipMethod': cartContent.shipping.code,
    'shippingCost': convertToUSD(cartContent.shipping.price),
    'currency': 'USD',
    'discount': convertToUSD(cartContent.discounts),
    'promoCode': cartContent.promotion_code,
    'products': getProducts(cartContent)
  }
  return order;
}

var getProducts = function(cartContent) {
  var prodArray = []
  cartContent.items.forEach(function(item) {
    var product = {
      'category': 'available',
      'id': item.product.product_code,
      'quantity': item.quantity,
      'price': (item.quantity * convertToUSD(item.sale_price)).toFixed(2)
    }
    prodArray.push(product);
  });

  return prodArray;
};

var urlBuilder = function(objURL) {
  var urlString;
  urlString = objURL.url + "?";

  objURL.params.forEach(function(item) {
    urlString += item.arg + "=" + encodeURIComponent(item.value) + "&";
  });
  
  urlString = urlString.substring(0, urlString.length-1);

  return urlString;
}

var isProduction = function() {

  var url = document.URL;
  
  if (url.match(/shop.lego.com/g)) {
    return true;
  }
  return false;
};

var getTrackmanEnvironmentScript = function(isTrackmanProd) {
  var src = 'https://mi-od-live-s.legocdn.com/r/www/r/analytics/Modules/TrackManApi?a=b';
  
  //Set src to QA
  if (!isTrackmanProd) {
    src = 'https://mi-od-qa-s.legocdn.com/r/www/r/analytics/Modules/TrackManApi';
  }
 
  	return src;
};

function getCookie(name) {
  var value = "; " + document.cookie;
  var parts = value.split("; " + name + "=");
  if (parts.length == 2) return parts.pop().split(";").shift();
}
function npsSurveryCounter() {
  var localeArray = ['en-GB', 'en-US', 'en-CA', 'de-DE'];
  var displayPageCount = _satellite.getVar('surveyPageCountLimit');
  var pageCount = _satellite.getVar('surveyPageCount');
  if(pageCount < 3) {
    if(localeArray.indexOf(_satellite.getVar('currentLocale')) !== -1) {
      pageCount++;
      _satellite.setVar('surveyPageCount', pageCount);
      if (pageCount === displayPageCount) {
        displaySurvey( _satellite.getVar('currentLocale') );
      }
  	}
  };
};
function displaySurvey( locale ) {
  if (locale == 'en-CA') {
    locale = 'en-US';
  }
  _satellite.notify('survery fired', 3);
  var surveyId = 'survey-'+ locale;
  var p, s;
  p = document.createElement('script');
  p.id = surveyId;
  p.type = 'text/javascript';
  p.src = document.location.protocol + '//lego.com/go/215/?context=shop&locale=' + locale;
  s = document.getElementsByTagName('script')[0];
  s.parentNode.insertBefore(p, s);
}

function createPreviousUrl(previousLocation){
	if(!previousLocation) {
		return null;
	}
	return window.location.protocol + '//' + window.location.hostname + previousLocation;
};

function getNewProducts(cartContent) {
  var prodArray = []
  cartContent.forEach(function(item) {
    var product = {
      'id': item.id,
      'quantity': item.quantity,
      'price': (item.quantity * convertToUSD(item.price)).toFixed(2)
    }
    prodArray.push(product);
  });

  return prodArray;
};

function checkDecible() {
  if(!_satellite.getVar('decibleLoaded')) {
    
    return;
  }
  window.decibelInsight('setCollection', false, false);
}

