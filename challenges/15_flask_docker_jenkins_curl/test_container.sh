#curl test script

status_code=$(curl -ks \
-w "%{http_code}" \
-o /dev/null \
"http://172.17.0.2:5050/")

echo $status_code

if [ $status_code -eq 200 ]
then 
   echo "Yes - FlaskApp is running - returning status code: 200"
else
   echo "No - FlaskApp is down - returning status code: $status_code"
fi