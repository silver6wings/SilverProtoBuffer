import { timestamp } from 'types';
import { set } from 'lodash';
import { ALL } from './constants';
import env from './env';
import fakeData from './fakeData';

// ==========================
//   Backend Request Below
// ==========================
const envApiHost = {
  Local: 'http://localhost:8088',
  Stage: 'https://video-metrics-api.staging.hulu.com',
  Prod: 'https://video-metrics-api.prod.hulu.com',
};
const apiHost = env.HULU_ENV === 'prod' ? envApiHost.Prod : envApiHost.Stage;

/* eslint-disable @typescript-eslint/no-explicit-any */
const request = (url: string, method: string = 'GET', body?: any): Promise<any> => {
  return fetch(url, {
    credentials: 'include',
    method,
    headers: {
      accept: 'application/json',
      'Content-Type': 'application/json',
    },
    body,
  }).then(res => {
    const json = res.json();
    if (res.status !== 200) {
      return json.then(content => Promise.reject(content));
    }
    return json;
  });
};

const requestWithFake = (fakeJson: object): Function => {
  if (env.HULU_ENV === 'development') {
    return (): Promise<any> => {
      return new Promise((resolve): any => {
        resolve(fakeJson);
      });
    };
  }
  return request;
};

const buildUrlWithParams = (url: string, params: any): string => {
  const kvPairs = Object.keys(params).reduce((list: string[], key: string): string[] => {
    if (!params[key] || params[key] === ALL) {
      return list;
    }
    list.push(`${key}=${params[key]}`);
    return list;
  }, []);
  return `${url}?${kvPairs.join('&')}`;
};

/* eslint-disable @typescript-eslint/no-unused-vars */
/* eslint-disable @typescript-eslint/camelcase */
const requests = {
  getMessages: (): Promise<any> => {
    return request(`${apiHost}/api/messages`);
  },

  getIncidents: (from: timestamp, to?: timestamp, severity?: number): Promise<any> => {
    return request(buildUrlWithParams(`${apiHost}/api/incidents`, { from, to, severity })).then(
      (json: any): any => json.incidents,
    );
  },

  getConvivaAlerts: (from: timestamp, to?: timestamp, severity?: number): Promise<any> => {
    return request(buildUrlWithParams(`${apiHost}/api/conviva_quality_alerts`, { from, to })).then(
      (json: any): any => json.alerts,
    );
  },

  getDataIssues: (from: timestamp, to: timestamp, data_source: string): Promise<any> => {
    return request(buildUrlWithParams(`${apiHost}/api/data_issues`, { from, to, data_source })).then(
      (json: any): any => json.issues,
    );
  },

  getSummary: (
    from: timestamp,
    metric: string,
    data_source: string,
    to?: timestamp,
    content_bundle_type?: string,
    live_stream_provider?: string,
    device_platform?: string,
    player_device_platform?: string,
    upper_severity?: string,
    cdn?: string,
  ): Promise<any> => {
    const params = {
      from,
      metric,
      data_source,
      to,
      device_platform,
      player_device_platform,
      content_bundle_type,
      live_stream_provider,
      upper_severity,
      cdn,
    };
    return request(buildUrlWithParams(`${apiHost}/api/summary`, params)).then((json: any): any => json.qos_summary);
  },

  getClientReleases: (from: timestamp, to?: timestamp, device_platform?: string): Promise<any> => {
    const params = { from, to, device_platform };
    return request(buildUrlWithParams(`${apiHost}/api/client_releases`, params)).then(
      (json: any): any => json.client_releases,
    );
  },

  getBackendReleases: (from: timestamp, to?: timestamp, team?: string): Promise<any> => {
    const params = { from, to, team };
    return request(buildUrlWithParams(`${apiHost}/api/backend_releases`, params)).then(
      (json: any): any => json.backend_releases,
    );
  },

  getConvivaUserSessions: (from: timestamp, to?: timestamp, userId?: string, userEmail?: string): Promise<any> => {
    const params = {
      from: Math.floor(from / 1000),
      to: Math.floor(to / 1000),
    };
    if (userEmail) {
      set(params, 'email', userEmail);
    } else {
      set(params, 'user_id', userId);
    }

    return request(buildUrlWithParams(`${apiHost}/api/viewer_sessions`, params));
  },

  getQosMetrics: (
    from: timestamp,
    content_bundle_type: string,
    live_stream_provider: string,
    metric: string,
    data_source: string,
    granularity?: string,
    to?: timestamp,
    device_platform?: string,
    player_device_platform?: string,
    cdn?: string,
    content_package_id?: string,
  ): Promise<any> => {
    const params = {
      from,
      content_bundle_type,
      live_stream_provider,
      metric,
      granularity,
      to,
      device_platform,
      player_device_platform,
      data_source,
      cdn,
      content_package_id,
    };

    return request(buildUrlWithParams(`${apiHost}/api/qos_metrics`, params));
  },

  getQosMetricsDelay: (
    content_bundle_type: string,
    live_stream_provider: string,
    metric: string,
    granularity?: string,
    device_platform?: string,
    player_device_platform?: string,
    data_source?: string,
    cdn?: string,
    content_package_id?: string,
  ): Promise<any> => {
    const params = {
      content_bundle_type,
      live_stream_provider,
      metric,
      granularity,
      device_platform,
      player_device_platform,
      data_source,
      cdn,
      content_package_id,
    };

    return request(buildUrlWithParams(`${apiHost}/api/qos_metrics_delay`, params));
  },

  getSuperBowlMetrics: (
    from: timestamp,
    metric: string,
    filter_id: string,
    to?: timestamp,
    granularity?: string,
  ): Promise<any> => {
    const params = {
      from,
      metric,
      filter_id,
      to,
      granularity,
    };
    return requestWithFake({})(buildUrlWithParams(`${apiHost}/api/qos_metrics`, params));
  },

  getRealTimePipelineStatus: (): Promise<any> =>
    requestWithFake(fakeData.getRealTimePipelineStatus)(`${apiHost}/api/pipeline_status`),

  getPlaybackExperienceStatus: (): Promise<any> =>
    requestWithFake(fakeData.getPlaybackExperienceStatus)(`${apiHost}/api/experience_status`),

  getPlaybackFunctionStatus: (): Promise<any> =>
    requestWithFake(fakeData.getPlaybackFunctionStatus)(`${apiHost}/api/function_status`),

  getDataBreakDown: (): Promise<any> => requestWithFake(fakeData.getDataBreakDown)(`${apiHost}/api/data_breakdown`),

  getSherlockPSS: (
    from: string,
    to?: string,
    user_id?: string,
    user_email?: string,
    device_platform?: string,
    player_device_platform?: string,
  ): Promise<any> => {
    const param = {
      from,
      to,
      user_id,
      user_email,
      device_platform,
      player_device_platform,
    };
    return requestWithFake(fakeData.getSherlockPSS)(buildUrlWithParams(`${apiHost}/api/playback_sessions`, param));
  },

  getSherlockPlaybackEvents: (
    from: string,
    to?: string,
    user_id?: string,
    user_email?: string,
    event_types?: string,
  ): Promise<any> => {
    const param = {
      from,
      to,
      user_id,
      user_email,
      event_types,
    };
    return requestWithFake(fakeData.getSherlockPEvents)(buildUrlWithParams(`${apiHost}/api/playback_events`, param));
  },

  getLiveSignalIndicator: (from: timestamp, to?: timestamp, granularity?: string): Promise<any> => {
    return request(buildUrlWithParams(`${apiHost}/api/indicator_per_provider`, { from, to, granularity })).then(
      (json: any): any => json.indicators,
    );
  },
};

/* eslint-enable @typescript-eslint/camelcase */
/* eslint-enable @typescript-eslint/no-unused-vars */

/* eslint-enable @typescript-eslint/no-explicit-any */

export { requests };
