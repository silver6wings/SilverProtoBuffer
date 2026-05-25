const fetchLotrGraphQL = (query: string, variables: object): Promise<object> => {
  return fetch('https://lotr.prod.hulu.com/graphql', {
    method: 'POST',
    // @ts-ignore
    headers: {
      'X-Internal-Mode': true,
      'Content-Type': 'application/json',
      Accept: 'application/json',
    },
    body: JSON.stringify({
      query,
      variables,
    }),
  });
};

const getThirdPartyQuery = `query ($startsAfter: String!, $endsBefore: String!) {
  changeRequests(filter: {startsAfter: $startsAfter, endsBefore: $endsBefore}) {
    id
    number
    shortDescription
    type
    category
    approval
    startsAt
    endsAt
    closedAt
    __typename
  }
}`;

const getKeyLinearEventQuery = `query ($startsAfter: String!, $endsBefore: String!) {
  cmnScheduleBlackouts {
    id   
    name
    description
    spans(filter: {startsAfter: $startsAfter, endsBefore: $endsBefore}) {
      id
      name
      startsAt
      endsAt
      __typename
    }
    __typename
  }
}`;

/* eslint-disable @typescript-eslint/no-explicit-any */

export const lotrQraphQL = {
  // Sample Parameters Input:
  // const startsAfter = '2019-09-09T16:00:00.000Z';
  // const endsBefore = '2019-09-17T15:59:59.999Z';
  getThirdPartyNOC: (startsAfter: string, endsBefore: string): Promise<object> =>
    fetchLotrGraphQL(getThirdPartyQuery, { startsAfter, endsBefore }).then((r: any) => r.json()),
  getKeyLinearEvent: (startsAfter: string, endsBefore: string): Promise<object> =>
    fetchLotrGraphQL(getKeyLinearEventQuery, { startsAfter, endsBefore }).then((r: any) => r.json()),
};

/* eslint-enable @typescript-eslint/no-explicit-any */
