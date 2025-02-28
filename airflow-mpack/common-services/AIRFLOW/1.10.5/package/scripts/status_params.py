"""
Licensed to the Apache Software Foundation (ASF) under one
or more contributor license agreements.  See the NOTICE file
distributed with this work for additional information
regarding copyright ownership.  The ASF licenses this file
to you under the Apache License, Version 2.0 (the
"License"); you may not use this file except in compliance
with the License.  You may obtain a copy of the License at
    http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
Ambari Agent
"""

import os
from resource_management.libraries.script import Script
from resource_management.libraries.functions import format
from resource_management.libraries.functions.default import default

config = Script.get_config()

airflow_user = config['configurations']['airflow-env']['airflow_user']
airflow_group = config['configurations']['airflow-env']['airflow_group']
airflow_log_dir = config['configurations']['airflow-env']['airflow_log_dir']
airflow_pid_dir = config['configurations']['airflow-env']['airflow_pid_dir']
airflow_webserver_pid_file = config['configurations']['airflow-env']['airflow_pid_dir'] + '/webserver.pid'
airflow_scheduler_pid_file = config['configurations']['airflow-env']['airflow_pid_dir'] + '/scheduler.pid'
airflow_worker_pid_file = config['configurations']['airflow-env']['airflow_pid_dir'] + '/worker.pid'
airflow_kerberos_pid_file = config['configurations']['airflow-env']['airflow_pid_dir'] + '/kerberos.pid'
airflow_flower_pid_file = config['configurations']['airflow-env']['airflow_pid_dir'] + '/flower.pid'
