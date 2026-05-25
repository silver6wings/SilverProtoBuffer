export const DASHBOARDS = {
  IMPACT: 'Impact',
  EVENT_ANALYSIS: 'EventAnalysis',
  REAL_TIME: 'RealTime',
  SHERLOCK: 'Sherlock',
  DATA_CROSS_CHECK: 'DataCrossCheck',
};

export const CONNECT_GROUP = {
  SuperBowl: 'connect_group',
  Sherlock: 'sherlock_group',
};

export const OVERVIEW_DATE_RANGE = {
  today: 'Today',
  yesterday: 'Yesterday',
  lastWeek: 'Last Week',
  lastMonth: 'Last Month',
};

export const SUPERBOWL_DATE_RANGE = {
  today: 'Today',
  last2Hours: 'Past 2 hours',
  last6Hours: 'Past 6 hours',
  last24Hours: 'Past 24 hours',
  last3Days: 'Past 3 Days',
};

export const SHERLOCK_DATE_RANGE = {
  today: 'Today',
  yesterday: 'Yesterday',
  last3Days: 'Last 3 Days',
  lastWeek: 'Last Week',
};

export const SEVERITY_COLOR = ['#FF0202', '#FF9800', '#EEBB16', '#EEE116', '#FFFFFF'];

export const LIVE_SIGNAL_QUALITY_INDICATOR_COLOR = ['#568BED', '#ED568B', '#EBB164'];

export const LIVE_PROVIDER_NAMES: { [key: string]: string } = {
  isp: 'iStreamPlanet',
  mlb: 'DSS',
  sync: 'Syncbak',
};

export const SESSION_STATES = {
  VSF: 'VSF',
  VPF: 'VPF',
  EBVS: 'EBVS',
  PLAYED: 'PLAYED',
};

export const SESSION_STATE_COLOR = {
  VSF: '#900C3F',
  VPF: '#FF5733',
  EBVS: '#5DADE2',
  PLAYED: '#2ECC71',
};

export const FONT_FAMILY =
  "Graphik, -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, 'Microsoft Yahei', sans-serif";

export const FONT_STYLE_CHART_TITLE = {
  fontFamily: FONT_FAMILY,
  fontSize: 18,
  fontWeight: 500,
};

export const FONT_STYLE_CHART_SUBTITLE = {
  fontFamily: FONT_FAMILY,
  fontSize: 15,
  color: '#777',
};

export const FONT_STYLE_CHART_AXIS_DATA = {
  fontFamily: FONT_FAMILY,
  fontSize: 14,
  fontWeight: 400,
};

export const FONT_STYLE_CHART_TOOLTIP = {
  fontFamily: FONT_FAMILY,
  fontSize: 12,
  fontWeight: 400,
};

export const FILTER_LABEL = {
  timeRange: 'Timeline Range',
  dataSource: 'Data Source',
  devicePlatform: 'Device Platform',
  playerDevicePlatform: 'Player Device Platform',
  contentBundleType: 'Content Bundle Type',
  liveStreamProvider: 'Live Stream Provider',
  metric: 'Metric',
  otherMetric: 'Other Metric',
  cdn: 'CDN',
  contentPackageID: 'Content Package ID',
};

export const ALL = 'All';

export const CONTENT_BUNDLE_TYPES = {
  all: ALL,
  vod: 'VOD',
  live: 'Live',
};

export const CDN = {
  all: ALL,
  fastly: 'Fastly',
  edgecast: 'Edgecast',
  akamai: 'Akamai',
  level3: 'Level3',
  Cloudfront: 'Cloudfront',
};

export const CONTENT_PACKAGE_ID = {
  all: ALL,
};

export const METRIC = {
  vpf: 'VPF',
  vsf: 'VSF',
  cirr: 'CIRR',
  vst: 'VST',
  ebvs: 'EBVS',
  cireph: 'CIREpH',
  lpeel: 'LPEEL',
  pbr: 'PBR',
};

export const OTHER_METRIC = {
  ConcurrentPlays: 'ConcurrentPlays',
  Attempts: 'Attempts',
  EndedPlays: 'EndedPlays',
  Bitrate: 'Bitrate',
  StartupError: 'StartupError',
  PlaybackError: 'PlaybackError',
};

export const LIVE_STREAM_PROVIDER = {
  all: ALL,
  iStreamPlanet: 'iStreamPlanet',
  dss: 'DSS',
  syncbak: 'Syncbak',
};

export const DEVICE_PLATFORM = {
  all: ALL,
  android: 'Android',
  iOS: 'iOS',
  tvOS: 'tvOS',
  george: 'George',
  roku: 'Roku',
  web: 'Web',
  chromecast: 'Chromecast',
};

/* player device platform type start */
export const Android = {
  all: ALL,
  android: 'Hulu Android',
  kindleFire: 'Hulu Kindle Fire',
  androidTV: 'Hulu AndroidTV',
};

export const iOS = {
  all: ALL,
  iOS: 'Hulu iOS',
  airplay: 'Hulu AirPlay',
};

export const tvOS = {
  all: ALL,
  tvOS: 'Hulu tvOS',
};

export const George = {
  all: ALL,
  george: 'Hulu George',
  fireTV: 'Hulu FireTV',
  ps3: 'Hulu PS3',
  ps4: 'Hulu PS4',
  xBoxOne: 'Hulu Xbox One',
  xBox360: 'Hulu Xbox 360',
  lgWebOS: 'Hulu LG WebOS',
  xfinity: 'Hulu Xfinity',
  samsungTizen: 'Hulu Samsung Tizen',
  vizioSametCast: 'Hulu Vizio SmartCast',
  nintendoSwtich: 'Hulu Nintendo Switch',
};

export const Roku = {
  all: ALL,
  roku: 'Hulu Roku',
  echoshow: 'Hulu EchoShow',
};

export const Web = {
  all: ALL,
  web: 'Hulu Web',
  webDash: 'Hulu Web DASH',
  webHLS: 'Hulu Web HLS',
};

export const Chromecast = {
  all: ALL,
  chromecast: 'Hulu Chromecast',
};
/* player device platform type end */

export const PLAYER_DEVICE_PLATFORM = {
  all: ALL,
  Android,
  iOS,
  tvOS,
  George,
  Roku,
  Web,
  Chromecast,
};

export const CLIENTS = ['Android', 'iOS', 'tvOS', 'George', 'Roku', 'Web', 'Chromecast'];

export const BACKEND_TEAMS = ['Play Stack', 'Live Pipeline', 'VOD Pipeline', 'AV Metadata', 'Playback Intelligence'];

export const CONVIVA_METRIC = ['VPF', 'VSF', 'VST', 'CIRR', 'EBVS'];

export const DATA_STATES = {
  LOADING: 0,
  SUCCESS: 1,
  ERROR: 2,
};

export const TIME_ZONE = {
  LosAngeles: 'America/Los_Angeles',
  NewYork: 'America/New_York',
  Beijing: 'Asia/Shanghai',
  GMT: 'Etc/GMT',
  Local: '',
};

export const DATA_SOURCE = {
  Hit: 'HIT',
  Conviva: 'Conviva',
  Shield: 'SHIELD',
};

export const GRANULARITY_VALUES = {
  OneDay: '1440',
  OneHour: '60',
  HalfHour: '30',
  FiveMinute: '5',
  FifteenMinute: '15',
  OneMinute: '1',
};

export const STATUS_COLORS: StatusColorMap = {
  none: 'grey',
  healthy: 'green',
  warning: 'orange',
  error: 'red',
};

export interface StatusColorMap {
  [key: string]: string;
}

export const EVENT_ACTION = {
  ChangeTimeRange: 'Change time range',
  ClickFilter: 'Click filter',
};

export const FILTER_OPTION_TYPE = {
  SubGroup: 'Sub group',
};

export const USER_INPUT_TYPES = {
  USER_ID: 'User ID',
  USER_EMAIL: 'User Email',
};

export const FILTER_DEVICE_PLATFORMS = {
  Android: ['Hulu Android', 'Hulu Android Phone', 'Hulu Kindle Fire'],
  iOS: ['Hulu iOS', 'Hulu AirPlay'],
  tvOS: ['Hulu tvOS'],
  George: [
    'Hulu Xbox One',
    'Hulu FireTV',
    'Hulu Nintendo Switch',
    'Hulu Xbox 360',
    'Hulu PS3',
    'Hulu PS4',
    'Hulu George',
    'Hulu Xfinity',
    'Hulu Vizio SC',
    'Hulu Samsung Tizen',
    'Hulu LG WebOS',
    'Hulu AndroidTV',
  ],
  Scarlet: ['Hulu EchoShow'],
  Roku: ['Hulu Roku', 'Hulu Roku Liberty TV', 'Hulu Roku Littlefield'],
  Web: ['Hulu Web', 'Hulu Web DASH', 'Hulu Web HLS'],
  Chromecast: ['Hulu Chromecast'],
};

export const FILTER_LIVE_STREAM_PROVIDERS = {
  iStreamPlanet: 'ISP',
  DSS: 'MLB',
  Syncbak: 'SYNC',
};

export const PLAYER_EVENT_TYPES: Record<string, string> = {
  // PlayerSessionSummary: 'player_session_summary',
  // PlayerSessionProgress: 'player_session_progress',
  PlayerBufferEnd: 'player_buffer_end',
  PlayerBufferStart: 'player_buffer_start',
  PlayerCdnChanged: 'player_cdn_changed',
  PlayerContentEnd: 'player_content_end',
  PlayerContentStart: 'player_content_start',
  PlayerError: 'player_error',
  PlayerMbrModeChanged: 'player_mbr_mode_changed',
  PlayerQualityChanged: 'player_quality_changed',
  PlayerSegmentStart: 'player_segment_start',
  PlayerSegmentEnd: 'player_segment_end',
  PlayerStart: 'player_start',
  PlayerStartupTime: 'player_startup_time',
  PlayerPause: 'player_pause',
  PlayerSeekStart: 'player_seekstart',
  PlayerSeekEnd: 'player_seekend',
  PlayerContinuousPlaySwitch: 'player_continuousplay_switch',
  PlayerHeartBeat: 'player_heartbeat',
  PlayerResume: 'player_resume',
  PlayerCustomEvent: 'player_custom_event',
};

export const API_ERROR_CODE: Record<string, number> = {
  InputError: 1000,
  SSOError: 1001,
  PermissionError: 1002,
  TutError: 1003,
  WriteError: 1004,
};

export const DATA_DELAY_UNKNOWN = -1;

export const PARAMS = {
  tab: 'tab',
  timeRange: 'timeRange',
  startTime: 'startTime',
  endTime: 'endTime',
  dataSource: 'dataSource',
  devicePlatform: 'devicePlatform',
  playerDevicePlatform: 'playerDevicePlatform',
  contentBundleType: 'contentBundleType',
  liveStreamProvider: 'liveStreamProvider',
  cdn: 'cdn',
  contentPackageID: 'contentPackageID',
  metric: 'metric',
  granularity: 'granularity',
  incLevelsStr: 'incLevelsStr',
  qosImpacted: 'qosImpacted',
  incDuration: 'incDuration',
  userInputType: 'userInputType',
  userQuery: 'userQuery',
};
