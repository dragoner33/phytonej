#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2

class MainHandler(webapp2.RequestHandler):
    def post(self):
        km = self.request.get("km", 0)
        tiempo = self.request.get("tiempo", 1)
        consumomed = self.request.get("consumomed", 0)
        velmed = int(km) / int(tiempo)
        consumototal = int(km) * int(consumomed)
        self.response.write("La velocidad media es: " + str(velmed) + " km/h y el consumo total es: " + str(consumototal) + " litros")

        if len(km.strip()) == 0:
            km = 0
        if len(tiempo.strip()) == 0:
            tiempo = 1
        if len(consumomed.strip()) == 0:
            consumomed = 0
        if km < 0:
            km = 0
        if tiempo <= 0:
            tiempo = 1
        if consumomed < 0:
            consumomed = 0



app = webapp2.WSGIApplication([
    ('/consumo', MainHandler)
], debug=True)
