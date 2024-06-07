import matplotlib.pyplot as plt
from datetime import datetime

# SSHD logs data
sshd_logs = [
    "[2024-01-19 12:59:11] Server listening on 0.0.0.0 port 2221.",
    "[2024-01-19 12:59:11] Server listening on :: port 2221.",
    "[2024-01-28 15:24:23] Connection from 100.72.1.95 port 47721 on 100.107.36.130 port 2221 rdomain ''",
    "[2024-01-28 15:24:24] Failed publickey for root from 100.72.1.95 port 47721 ssh2: ECDSA SHA256:E5niDfUPHiDYyqgzSsVH_pHW3lKVqGnZTlPDIXoK5sU",
    "[2024-01-28 15:24:33] Failed password for root from 100.72.1.95 port 47721 ssh2",
    "[2024-01-28 15:24:39] Failed password for root from 100.72.1.95 port 47721 ssh2",
    "[2024-01-28 15:24:43] Failed password for root from 100.72.1.95 port 47721 ssh2",
    "[2024-01-28 15:24:43] Connection closed by authenticating user root 100.72.1.95 port 47721 [preauth]",
    "[2024-02-13 11:29:50] Connection from 100.81.51.199 port 63172 on 100.107.36.130 port 2221 rdomain ''",
    "[2024-02-13 11:29:50] Accepted password for root from 100.81.51.199 port 63172 ssh2",
    "[2024-02-13 11:29:50] Starting session: shell on pts/2 for root from 100.81.51.199 port 63172 id 0",
    "[2024-02-13 11:57:16] syslogin_perform_logout: logout() returned an error",
    "[2024-02-13 11:57:16] Received disconnect from 100.81.51.199 port 63172:11: disconnected by user",
    "[2024-02-13 11:57:16] Disconnected from user root 100.81.51.199 port 63172",
    "[2024-02-15 10:40:47] Connection from 101.111.18.92 port 44711 on 100.107.36.130 port 2221 rdomain ''",
    "[2024-02-15 10:40:48] Failed publickey for softdev from 101.111.18.92 port 44711 ssh2: ECDSA SHA256:TMRAzI8Xehi9UN05pl5PypfDmgKC_5TDKW01T03k6H0",
    "[2024-02-15 10:40:50] Accepted password for softdev from 101.111.18.92 port 44711 ssh2",
    "[2024-02-15 10:40:51] Starting session: shell on pts/2 for softdev from 101.111.18.92 port 44711 id 0",
    "[2024-02-15 10:42:20] syslogin_perform_logout: logout() returned an error",
    "[2024-02-15 10:42:20] Received disconnect from 101.111.18.92 port 44711:11: disconnected by user",
    "[2024-02-15 10:42:20] Disconnected from user softdev 101.111.18.92 port 44711",
    "[2024-02-15 18:51:47] Connection from 101.111.18.92 port 44711 on 100.107.36.130 port 2221 rdomain ''",
    "[2024-02-15 18:51:48] Failed publickey for softdev from 101.111.18.92 port 44711 ssh2: ECDSA SHA256:TMRAzI8Xehi9UN05pl5PypfDmgKC_5TDKW01T03k6H0",
    "[2024-02-15 18:51:50] Accepted password for softdev from 101.111.18.92 port 44711 ssh2",
    "[2024-02-15 18:51:51] Starting session: shell on pts/2 for softdev from 101.111.18.92 port 44711 id 0",
    "[2024-02-15 18:59:39] syslogin_perform_logout: logout() returned an error",
    "[2024-02-15 18:59:39] Received disconnect from 101.111.18.92 port 44711:11: disconnected by user",
    "[2024-02-15 18:59:39] Disconnected from user softdev 101.111.18.92 port 44711",
    "[2024-02-16 10:26:47] Connection from 100.86.71.224 port 58713 on 100.107.36.130 port 2221 rdomain ''",
    "[2024-02-16 10:26:48] Failed publickey for softdev from 100.86.71.224 port 58713 ssh2: ECDSA SHA256:p2aapGz1SWK8ioSXxVzrvI4qKjpCPLIj2e421Wf4Hk8",
    "[2024-02-16 10:26:50] Accepted password for softdev from 100.86.71.224 port 58713 ssh2",
    "[2024-02-16 10:26:51] Starting session: shell on pts/2 for softdev from 100.86.71.224 port 58713 id 0",
    "[2024-02-16 14:47:28] syslogin_perform_logout: logout() returned an error",
    "[2024-02-16 14:47:28] Received disconnect from 100.86.71.224 port 58713:11: disconnected by user",
    "[2024-02-16 14:47:28] Disconnected from user softdev 100.86.71.224 port 58713",
    "[2024-02-19 04:00:14] Connection from 2.67.182.119 port 60071 on 100.107.36.130 port 2221 rdomain ''",
    "[2024-02-19 04:00:14] Failed publickey for root from 2.67.182.119 port 60071 ssh2: ECDSA SHA256:8emchJ7sq-LAes1f_hYMEVJzOYv36Aa5xkgG5aD5nl8",
    "[2024-02-19 04:00:15] Failed password for root from 2.67.182.119 port 60071 ssh2",
    "[2024-02-19 04:00:17] Failed password for root from 2.67.182.119 port 60071 ssh2",
    "[2024-02-19 04:00:18] Failed password for root from 2.67.182.119 port 60071 ssh2",
    "[2024-02-19 04:00:18] Connection closed by authenticating user root 2.67.182.119 port 60071 [preauth]",
    "[2024-02-21 09:55:33] Connection from 100.81.51.199 port 35991 on 100.107.36.130 port 2221 rdomain ''",
    "[2024-02-21 09:55:34] Failed publickey for root from 100.81.51.199 port 35991 ssh2: ECDSA SHA256:UyI8gqj5r-LvJgYLB0Nv_3ekzmWqO5rgwBdPnpKdRwY",
    "[2024-02-21 09:55:36] Failed password for root from 100.81.51.199 port 35991 ssh2",
    "[2024-02-21 09:55:38] Failed password for root from 100.81.51.199 port 35991 ssh2",
    "[2024-02-21 09:55:39] Failed password for root from 100.81.51.199 port 35991 ssh2",
    "[2024-02-21 09:55:39] Connection closed by authenticating user root 100.81.51.199 port 35991 [preauth]",
    "[2024-02-23 02:26:07] Connection from 2.67.182.119 port 46086 on 100.107.36.130 port 2221 rdomain ''",
    "[2024-02-23 02:26:08] Failed publickey for root from 2.67.182.119 port 46086 ssh2: ECDSA SHA256:8emchJ7sq-LAes1f_hYMEVJzOYv36Aa5xkgG5aD5nl8",
    "[2024-02-23 02:26:09] Failed password for root from 2.67.182.119 port 46086 ssh2",
    "[2024-02-23 02:26:11] Failed password for root from 2.67.182.119 port 46086 ssh2",
    "[2024-02-23 02:26:11] Failed password for root from 2.67.182.119 port 46086 ssh2",
    "[2024-02-23 02:26:11] Connection closed by authenticating user root 2.67.182.119 port 46086 [preauth]",
    "[2024-02-23 09:52:21] Connection from 101.111.18.92 port 34945 on 100.107.36.130 port 2221 rdomain ''",
    "[2024-02-23 09:52:21] Failed publickey for softdev from 101.111.18.92 port 34945 ssh2: ECDSA SHA256:TMRAzI8Xehi9UN05pl5PypfDmgKC_5TDKW01T03k6H0",
    "[2024-02-23 09:52:22] Accepted password for softdev from 101.111.18.92 port 34945 ssh2",
    "[2024-02-23 09:52:23] Starting session: shell on pts/2 for softdev from 101.111.18.92 port 34945 id 0",
    "[2024-02-23 10:00:30] syslogin_perform_logout: logout() returned an error",
    "[2024-02-23 10:00:30] Received disconnect from 101.111.18.92 port 34945:11: disconnected by user",
    "[2024-02-23 10:00:30] Disconnected from user softdev 101.111.18.92 port 34945",
    "[2024-02-23 10:29:17] Connection from 101.111.18.92 port 34945 on 100.107.36.130 port 2221 rdomain ''",
    "[2024-02-23 10:29:18] Failed publickey for softdev from 101.111.18.92 port 34945 ssh2: ECDSA SHA256:TMRAzI8Xehi9UN05pl5PypfDmgKC_5TDKW01T03k6H0",
    "[2024-02-23 10:29:20] Accepted password for softdev from 101.111.18.92 port 34945 ssh2",
    "[2024-02-23 10:29:21] Starting session: shell on pts/2 for softdev from 101.111.18.92 port 34945 id 0",
    "[2024-02-23 10:30:15] syslogin_perform_logout: logout() returned an error",
    "[2024-02-23 10:30:15] Received disconnect from 101.111.18.92 port 34945:11: disconnected by user",
    "[2024-02-23 10:30:15] Disconnected from user softdev 101.111.18.92 port 34945",
    "[2024-02-25 04:29:44] Connection from 101.111.18.92 port 34945 on 100.107.36.130 port 2221 rdomain ''",
    "[2024-02-25 04:29:44] Failed publickey for softdev from 101.111.18.92 port 34945 ssh2: ECDSA SHA256:TMRAzI8Xehi9UN05pl5PypfDmgKC_5TDKW01T03k6H0",
    "[2024-02-25 04:29:45] Accepted password for softdev from 101.111.18.92 port 34945 ssh2",
    "[2024-02-25 04:29:46] Starting session: shell on pts/2 for softdev from 101.111.18.92 port 34945 id 0",
    "[2024-02-25 04:29:46] syslogin_perform_logout: logout() returned an error",
    "[2024-02-25 04:29:46] Received disconnect from 101.111.18.92 port 34945:11: disconnected by user",
    "[2024-02-25 04:29:46] Disconnected from user softdev 101.111.18.92 port 34945",
    "[2024-02-26 10:56:57] Connection from 100.107.36.130 port 51567 on 100.107.36.130 port 2221 rdomain ''",
    "[2024-02-26 10:56:58] Failed publickey for root from 100.107.36.130 port 51567 ssh2: ECDSA SHA256:gV0-C9FTffFfuj7hZmrzNsTLo4ydm9sEzrq2JvTMaZ0",
    "[2024-02-26 10:56:59] Failed password for root from 100.107.36.130 port 51567 ssh2",
    "[2024-02-26 10:57:01] Failed password for root from 100.107.36.130 port 51567 ssh2",
    "[2024-02-26 10:57:01] Failed password for root from 100.107.36.130 port 51567 ssh2",
    "[2024-02-26 10:57:01] Connection closed by authenticating user root 100.107.36.130 port 51567 [preauth]",
    "[2024-02-27 01:16:59] Connection from 127.0.0.1 port 54240 on 127.0.0.1 port 2221 rdomain ''",
    "[2024-02-27 01:17:00] Failed publickey for root from 127.0.0.1 port 54240 ssh2: ECDSA SHA256:G2kW6Y5XV3Ttth1pN5bZCzkRkUk31r9nGRs_8kU2Srg",
    "[2024-02-27 01:17:01] Failed password for root from 127.0.0.1 port 54240 ssh2",
    "[2024-02-27 01:17:03] Failed password for root from 127.0.0.1 port 54240 ssh2",
    "[2024-02-27 01:17:03] Failed password for root from 127.0.0.1 port 54240 ssh2",
    "[2024-02-27 01:17:03] Connection closed by authenticating user root 127.0.0.1 port 54240 [preauth]",
    "[2024-02-27 04:57:56] Connection from 1.2.3.4 port 47568 on 100.107.36.130 port 2221 rdomain ''",
    "[2024-02-27 04:57:56] Failed publickey for root from 1.2.3.4 port 47568 ssh2: ECDSA SHA256:gV0-C9FTffFfuj7hZmrzNsTLo4ydm9sEzrq2JvTMaZ0",
    "[2024-02-27 04:57:57] Failed password for root from 1.2.3.4 port 47568 ssh2",
    "[2024-02-27 04:57:59] Failed password for root from 1.2.3.4 port 47568 ssh2",
    "[2024-02-27 04:57:59] Failed password for root from 1.2.3.4 port 47568 ssh2",
    "[2024-02-27 04:57:59] Connection closed by authenticating user root 1.2.3.4 port 47568 [preauth]",
    "[2024-02-28 12:32:21] Connection from 101.111.18.92 port 49220 on 100.107.36.130 port 2221 rdomain ''",
    "[2024-02-28 12:32:22] Failed publickey for softdev from 101.111.18.92 port 49220 ssh2: ECDSA SHA256:TMRAzI8Xehi9UN05pl5PypfDmgKC_5TDKW01T03k6H0",
    "[2024-02-28 12:32:23] Accepted password for softdev from 101.111.18.92 port 49220 ssh2",
    "[2024-02-28 12:32:24] Starting session: shell on pts/2 for softdev from 101.111.18.92 port 49220 id 0",
    "[2024-02-28 12:33:06] syslogin_perform_logout: logout() returned an error",
    "[2024-02-28 12:33:06] Received disconnect from 101.111.18.92 port 49220:11: disconnected by user",
    "[2024-02-28 12:33:06] Disconnected from user softdev 101.111.18.92 port 49220",
    "[2024-03-01 06:55:42] Connection from 101.111.18.92 port 49220 on 100.107.36.130 port 2221 rdomain ''",
    "[2024-03-01 06:55:43] Failed publickey for softdev from 101.111.18.92 port 49220 ssh2: ECDSA SHA256:TMRAzI8Xehi9UN05pl5PypfDmgKC_5TDKW01T03k6H0",
    "[2024-03-01 06:55:45] Accepted password for softdev from 101.111.18.92 port 49220 ssh2",
    "[2024-03-01 06:55:46] Starting session: shell on pts/2 for softdev from 101.111.18.92 port 49220 id 0",
    "[2024-03-01 06:55:47] syslogin_perform_logout: logout() returned an error",
    "[2024-03-01 06:55:47] Received disconnect from 101.111.18.92 port 49220:11: disconnected by user",
    "[2024-03-01 06:55:47] Disconnected from user softdev 101.111.18.92 port 49220",
    "[2024-03-02 05:22:55] Connection from 101.111.18.92 port 49220 on 100.107.36.130 port 2221 rdomain ''",
    "[2024-03-02 05:22:55] Failed publickey for softdev from 101.111.18.92 port 49220 ssh"
]


# Parse SSHD logs and extract timestamps and outcomes
timestamps = []
outcomes = []  # 'success' or 'failure'

for log_entry in sshd_logs:
    # Extract timestamp from log entry
    timestamp_str = log_entry[1:20]  # Extract timestamp substring
    timestamp = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
    timestamps.append(timestamp)

    # Determine outcome of login attempt
    if "Failed" in log_entry:
        outcomes.append('failure')
    else:
        outcomes.append('success')

# Plotting the SSHD logs
plt.figure(figsize=(10, 8))
for i, (timestamp, outcome) in enumerate(zip(timestamps, outcomes)):
    color = 'red' if outcome == 'failure' else 'green'
    plt.scatter(timestamp, i, color=color)

# Formatting the plot
plt.yticks(range(len(timestamps)), [f"Attempt {i+1}" for i in range(len(timestamps))])
plt.title("SSHD Logs Timeline")
plt.xlabel("Timestamp")
plt.ylabel("Login Attempt")
plt.grid(axis='y')

# Displaying the plot
plt.show()
