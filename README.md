# Unique-Device-Tracker

An API to provide each device with a device fingerprint and store it in the DB, each call to the API will return either True or False
True - a new user
False - not a new user

API - 
https://rk123456.pythonanywhere.com/store/{id-here}

Below is the example to integrate in frontend -

**Simple js**

<script src="https://cdn.jsdelivr.net/npm/@fingerprintjs/fingerprintjs@3"></script>
<script>
  const fpPromise = import('https://openfpcdn.io/fingerprintjs/v4')
    .then(FingerprintJS => FingerprintJS.load())
  fpPromise
    .then(fp => fp.get())
    .then(result => {      
const visitorId = result.visitorId; 
const url = 'https://rk123456.pythonanywhere.com/store/' + visitorId; 
   fetch(url)
        .then(response => response.text())
        .then(data => console.log(data))
        .catch(error => console.error('Error fetching data:', error));
    })
    .catch(error => {
      console.error('Error getting visitor ID:', error);
    });
</script>



**Reactjs**

  useEffect(() => {
  fpPromise
    .then(fp => fp.get())
    .then(result => {
      const visitorId = result.visitorId;
  }, []);
