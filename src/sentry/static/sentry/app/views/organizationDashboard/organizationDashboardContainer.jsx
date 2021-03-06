import React from 'react';

import {PageContent, PageHeader} from 'app/styles/organization';
import {t} from 'app/locale';
import BetaTag from 'app/components/betaTag';
import Feature from 'app/components/acl/feature';
import PageHeading from 'app/components/pageHeading';
import NoProjectMessage from 'app/components/noProjectMessage';
import GlobalSelectionHeader from 'app/components/organizations/globalSelectionHeader';
import SentryTypes from 'app/sentryTypes';
import withOrganization from 'app/utils/withOrganization';

class OrganizationDashboardContainer extends React.Component {
  static propTypes = {
    organization: SentryTypes.Organization,
  };

  render() {
    const {organization, children} = this.props;

    return (
      <Feature features={['discover']} renderDisabled>
        <GlobalSelectionHeader organization={organization} />

        <PageContent>
          <NoProjectMessage organization={organization}>
            <PageHeader>
              <PageHeading withMargins>
                {t('Dashboards')} <BetaTag />
              </PageHeading>
            </PageHeader>

            {children}
          </NoProjectMessage>
        </PageContent>
      </Feature>
    );
  }
}
export default withOrganization(OrganizationDashboardContainer);
export {OrganizationDashboardContainer};
